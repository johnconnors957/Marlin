Import("env")
env.Append(LINKFLAGS=["--specs=nano.specs"])
extra_scripts = add_nanolib.py