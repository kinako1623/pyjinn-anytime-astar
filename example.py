from system.lib import minescript
import java, time

pathfinder = java.import_pyjinn_script("smooth_path.pyj")
path = pathfinder.get("goto")(-2, 71, -350)

while True:
        status = pathfinder.get("move_status")
        if status == "arrived":
            print("exit 0")
            break
        elif status == "failed":
            print("exit 1")
            break
        time.sleep(0.1)

time.sleep(4)
