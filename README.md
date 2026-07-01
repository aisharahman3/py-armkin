# armkin

Planar 2-link arm forward/inverse kinematics, Jacobian and DH transforms.

## Usage

```python
import armkin
print(tuple(round(v, 3) for v in armkin.forward(1.0, 1.0, 0.5, 0.5)))
```
