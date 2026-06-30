import os
import sys
import subprocess

try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
except AttributeError:
    pass

def run_script(script_path):
    print(f"\nRunning {os.path.basename(script_path)}...")
    try:
        # Configure PYTHONPATH and PYTHONIOENCODING so that the script can import backend and print unicode
        env = os.environ.copy()
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if "PYTHONPATH" in env:
            env["PYTHONPATH"] = project_root + os.pathsep + env["PYTHONPATH"]
        else:
            env["PYTHONPATH"] = project_root
        env["PYTHONIOENCODING"] = "utf-8"
            
        result = subprocess.run(
            [sys.executable, script_path], 
            capture_output=True, 
            text=True, 
            check=True,
            env=env
        )
        print(f"[OK] {os.path.basename(script_path)} completed successfully.")
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        print(f"[FAIL] {os.path.basename(script_path)} failed!")
        print("Stdout:\n", e.stdout)
        print("Stderr:\n", e.stderr)
        return False, e.stderr



def main():
    print("=" * 60)
    print("Starting Verification Suite for Deal-Analyzer-V3")
    print("=" * 60)
    
    test_dir = os.path.dirname(os.path.abspath(__file__))
    
    tests = [
        "test_insert.py",
        "test_retrival.py",
        "test_parser.py",
        "test_reranker.py"
    ]
    
    success = True
    results = {}
    
    for test in tests:
        path = os.path.join(test_dir, test)
        if os.path.exists(path):
            ok, output = run_script(path)
            results[test] = ok
            if not ok:
                success = False
        else:
            print(f"[WARN] Test script {test} not found!")
            results[test] = False
            success = False
            
    # Check test_analyzer separately since it requires API key
    analyzer_path = os.path.join(test_dir, "test_analyzer.py")
    if os.path.exists(analyzer_path):
        if not os.getenv("GEMINI_API_KEY"):
            print("\n[WARN] Skipping test_analyzer.py because GEMINI_API_KEY is not set in the environment.")
            results["test_analyzer.py"] = "SKIPPED"
        else:
            ok, output = run_script(analyzer_path)
            results["test_analyzer.py"] = ok
            if not ok:
                success = False

                
    print("\n" + "=" * 60)
    print("Test Summary:")
    print("=" * 60)
    for test, status in results.items():
        if status is True:
            print(f"  {test:<20} : PASS [OK]")
        elif status == "SKIPPED":
            print(f"  {test:<20} : SKIPPED [WARN] (No API Key)")
        else:
            print(f"  {test:<20} : FAIL [FAIL]")
    print("=" * 60)
    
    if success:
        print("All runnable tests passed!")
        sys.exit(0)
    else:
        print("Some tests failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()

