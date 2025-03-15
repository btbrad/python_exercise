import sys, os, datetime, time, html

print(sys.platform)
print(sys.version)

print(os.getcwd())
print(os.environ)
print(os.getenv("HOMEPATH"))

print(datetime.date.today())
print(datetime.date.today().day)

print(time.strftime("%H:%M"))
print(time.strftime("%A %p"))

print(html.escape("<script>script</script>"))