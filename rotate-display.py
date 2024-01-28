import time, rotatescreen as rs
pd = rs.get_primary_display()
# Continuously rotate the screen with different angles
# 105 168 285 345
angle_list = [0, 90, 180, 270, 90, 180, 90, 270]
# Infinite loop
while True:
    for i in range(5):
        for x in angle_list:        
            pd.rotate_to(x)
            time.sleep(0.5)