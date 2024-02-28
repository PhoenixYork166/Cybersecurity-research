// import statement
use std::env;

use std::io::{self, Write};

// Using Net Library allows us to use IpAddr
// Create TcpStream
use std::net::{IpAddr, TcpStream};

// process to manage whether our program shuts down
use std::process;
use std::str::FromStr;
use std::sync::mpsc::{Sender, channel};

// Multi-threaded
use std::thread;

// Max no. Ports we can sniff
const MAX: u16 = 65535;

// Creating a Struct to hold command-line inputs
// flag, ipaddr, threads 
struct Arguments {
    #[allow(dead_code)]
    flag: String,
    // Enum for IP_ADDR => IPv4 or IPv6
    ipaddr: IpAddr,
    threads: u16,
}

// Method to instantiate this Struct for command-line arguments
impl Arguments {
    fn new(args: &[String]) -> Result<Arguments, &'static str> {
        // Logic for creating an instance of `Arguments` goes here.
        if args.len() < 2 {
            return Err("not enough arguments");

        } else if args.len() > 4 {
            return Err("too many arguments");
        }

        let f = args[1].clone();
        if let Ok(ipaddr) = IpAddr::from_str(&f) {

            return Ok(Arguments { 
                flag: String::from(""), 
                ipaddr, 
                threads: 4
            });
        } else {
            // If cannot send back 'ipaddr', 'threads'
            let flag = args[1].clone();

            // if argument contains -h OR -help 
            // Ignore the rest arguments
            // AND print Usage: ...
            if flag.contains("-h") || flag.contains("-help") && args.len() == 2 {
                println!("Usage: -j to select how many threads you want\n-h or -help to show this help message");
                
                // Return an error after showing help
                return Err("help requested"); 

              // If user inputs -h OR -help & also other flags e.g. -j
            } else if flag.contains("-h") || flag.contains("-help") {

                // send Err to terminal: Too many arguments
                return Err("Too many arguments");

              // If -j IP Addr is specified                
            } else if flag.contains("-j") {
                
                let ipaddr = match IpAddr::from_str(&args[3]) {
                    // Unwrap value inside OK
                    Ok(s) => s,
                    Err(_) => return Err("Not a valid IP Addr; must be IPv4 or IPv6")
                };

                // when -j IP Addr args[1] is specified 
                // Change strings in threads position to u16
                let threads = match args[2].parse::<u16>() {
                    // Unwrap value inside OK
                    Ok(s) => s,
                    // If failed to parse
                    Err(_) => return Err("Failed to parse thread number")

                };

                return Ok(Arguments{
                    threads, 
                    flag, 
                    ipaddr
                });

            } else {
                return Err("Invalid Syntax");
            }

        }

    }
}

// Our scanner scales based on amount of threads we pass
fn scan(tx: Sender<u16>, start_port: u16, addr: IpAddr, num_threads: u16) {

    // Start port
    let mut port: u16 = start_port + 1;

    loop {

        // Pass in IP Addr, port we're scanning
        match TcpStream::connect((addr, port)) {
            Ok(_) => {
                // Signify user that this program's running Ok
                // by sending back ...
                print!(".");

                // We use IO inside of our thread here
                // Construct a handle to the standard output
                // of the current process
                // By flushing
                // Allow to send messages (Mutex) of shared data
                io::stdout().flush().unwrap();

                // This will then send back to our rx to Open port
                tx.send(port).unwrap();
            }
            Err(_) => {}
        };

        // If MAX Port - current Port <= our num_threads
        // 0 <= current thread
        // stop program
        if (MAX - port) <= num_threads {
            break;
        }

        // iterate port by num_threads
        port += num_threads;
    }
}


fn main() {
    //println!("Hello, world!");

    // Getting command-line arguments passed to the program
    let args: Vec<String> = env::args().collect();

    // Locating program name from command-line args
    let program = args[0].clone();

    // This 'arguments' () code block takes a closure
    let arguments = Arguments::new(&args).unwrap_or_else(
        |err| {
            // to check if err contains help
            if err.contains("help") {

                // Exit our program
                process::exit(0)

            } else {
                eprintln!("{} problem parsing arguments: {}", program, err);
                process::exit(0);
            }
        }
    );

    // Storing argument inputs 'threads'
    let num_threads = arguments.threads;

    // Storing argument input -j IP to 'addr'
    let addr = arguments.ipaddr;

    // Instantiating a channel
    // tx = transmittor
    // rx = receiver
    let (tx, rx) = channel();

    // Looping through each thread
    for i in 0..num_threads {
        // To let each of our thread has its own transmittor
        let tx = tx.clone();

        // Spawning our thread with a move closure
        thread::spawn(move || {
            scan(tx, i, addr, num_threads);
        });
    }

    // Create a Mutable out vector (empty vector)
    let mut out = vec![];

    // Drop our tx transmittor from this scope
    // tx is only in the other thread
    // thus tx is NOT in the main thread
    drop(tx);

    // Iterate through our receiver
    for p in rx {

        // Pushing current receiver to out vector
        out.push(p);
    }

    // an empty line (separator) between . & output
    println!("");
    
    // Sorting our out vector
    out.sort();
    for v in out {

        // Printing out each Open Port
        println!("{} is open", v);
    }
}


