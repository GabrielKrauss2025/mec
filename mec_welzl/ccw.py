import matplotlib.pyplot as plt
import numpy as np
import pytest

# given 3 points (a, b and c), we want to determine wheter c
# is to the right or to the left of the ray ab

def ccw(a : np.ndarray, b  : np.ndarray, c : np.ndarray) -> int:
    det = (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
    if det > 0:
        return -1
    elif det < 0:
        return 1
    return 0

if __name__ == '__main__':
    def test_ccw_r():
        points = np.array([[0, 0], [0.5, 1], [0.5, 0.5]])
        a, b, c = points[0], points[1], points[2]
        plt.figure()
        label = ccw(a, b, c)
        plt.plot(points[0:2, 0], points[0:2, 1], c = 'gray', zorder = 1, label = f'{label}')
        plt.scatter(a[0], a[1], c = 'red', label = 'a', s=80)
        plt.scatter(b[0], b[1], c = 'blue', label = 'b', s=80)
        plt.scatter(c[0], c[1], c = 'orange', label = 'c', s=80)
        plt.axis('off')
        plt.legend()
        plt.show()

    def test_ccw_l():
        points = np.array([[0, 0], [0.5, 1], [-0.5, 0.5]])
        a, b, c = points[0], points[1], points[2]
        plt.figure()
        label = ccw(a, b, c)
        plt.plot(points[0:2, 0], points[0:2, 1], c = 'gray', zorder = 1, label = f'{label}')
        plt.scatter(a[0], a[1], c = 'red', label = 'a', s=80)
        plt.scatter(b[0], b[1], c = 'blue', label = 'b', s=80)
        plt.scatter(c[0], c[1], c = 'orange', label = 'c', s=80)
        plt.axis('off')
        plt.legend()
        plt.show()

    test_ccw_r()
    test_ccw_l()
    


    
