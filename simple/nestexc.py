
def action2():
    print(1 + [])            # Generate TypeError

def action1():
    try:
        action2()
    except TypeError as x:        # Most recent matching try
        print('inner try')
        raise x

try:
    action1()
except TypeError:            # Here, only if action1 re-raises
    print('outer try')
