import os, subprocess, sys
here = os.path.dirname(os.path.abspath(__file__))
for script in ("check_w6.py", "check_w14.py", "check_inclusion.py", "check_table_claims.py"):
    print("=== running", script)
    r = subprocess.run([sys.executable, os.path.join(here, script)])
    if r.returncode: sys.exit("FAILED: " + script)
print("\nEVERYTHING PASSED")
