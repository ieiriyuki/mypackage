import foo
import incl


print(foo.bar.add_one(4))
print(foo.num.make_zeros(2))

try:
    print(foo.version)
except Exception:
    print("no")

incl.say_cow()
