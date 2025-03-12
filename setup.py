import subprocess
import sys


def run_command(command):
    try:
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip()


print("\n🔹 Python Path:", sys.executable)

# Check Python version
success, output = run_command([sys.executable, "--version"])
if success:
    print("✅ Python Version:", output)
else:
    print("❌ Python version error:", output)
    sys.exit(1)

# Check PyQt6
success, output = run_command([sys.executable, "-m", "pip", "show", "PyQt6"])
if success and output:
    print("\n✅ PyQt6 Found!")
    print(output)
else:
    print("\n⚠️ PyQt6 Not Found. Installing...")
    success, output = run_command([sys.executable, "-m", "pip", "install", "PyQt6"])
    if success:
        print("\n🎉 PyQt6 Installed Successfully!")
    else:
        print("\n❌ PyQt6 Installation Failed:", output)
        sys.exit(1)

# Test import
print("\n✅ Testing PyQt6 Import...")
test_code = "import PyQt6; print('🎉 PyQt6 is ready! Version:', PyQt6.__version__)"
success, output = run_command([sys.executable, "-c", test_code])
if success:
    print(output)
else:
    print("\n❌ PyQt6 Import Error:", output)
