import sys
from collections import defaultdict

def processGame(events, H):
    """
    events: list of tuples (player, frame, attack_value)
        player: 1 or 2
        frame: non-negative integer
        attack_value: positive integer
    H: starting HP for both players

    Returns: [hp1, hp2] with each clamped to min 0
    """
    events=sorted(events,key=lambda x:x[1])
    hp1=hp2=H
    i=0
    while i<len(events):
        f=events[i][1]
        while i<len(events) and events[i][1]==f:
            p,_,atk=events[i]
            if p==1:
                hp2-=atk
            else:
                hp1-=atk
            i+=1
        hp1=max(0,hp1); hp2=max(0,hp2)
        if hp1==0 or hp2==0:
            break
    return [hp1,hp2]


# --- Main execution block. DO NOT MODIFY ---
if __name__ == "__main__":
    try:
        H = int(input().strip())
        n = int(input().strip())
        events = []
        for _ in range(n):
            parts = input().strip().split()
            events.append((int(parts[0]), int(parts[1]), int(parts[2])))

        result = processGame(events, H)
        print(f"{result[0]} {result[1]}")

    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
