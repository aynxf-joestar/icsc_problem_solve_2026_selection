import sys

def generate_shape(n, shape):
    """
    Generates a geometric pattern on an n x n grid.

    Args:
        n: Grid size (n x n, always odd for diamond)
        shape: Either "checkerboard" or "diamond"

    Returns:
        A 2D list of integers (0 or 1) representing the pattern.
    """
    grid=[[0]*n for _ in range(n)]
    if shape=="checkerboard":
        for i in range(n):
            for j in range(n):
                grid[i][j]=(i+j)%2
    elif shape=="diamond":
        c=n//2
        for i in range(n):
            for j in range(n):
                if abs(i-c)+abs(j-c)<=c:
                    grid[i][j]=1
    return grid




# --- Main execution block. DO NOT MODIFY ---
if __name__ == "__main__":
    try:
        n = int(input().strip())
        shape = input().strip()

        result = generate_shape(n, shape)
        for row in result:
            print(" ".join(str(x) for x in row))

    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
