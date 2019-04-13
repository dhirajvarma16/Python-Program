import commands
mount = commands.getoutput('mount -v')
lines = mount.splitlines()
points = map(lambda line: line.split()[2], lines)
print points
