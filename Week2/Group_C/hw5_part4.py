
from pathlib import Path

def parse_log_file(file_path):
   path = Path(file_path)   # 解析文件名称;
   if not path.exists(): 
       raise FileNotFoundError(path)
   
   findings = []
   for line in path.read_text().splitlines():
       if "ERROR" in line or "ASSERT_FAIL" in line:
            print(f"Detected issue: {line.strip()}")
   return findings

if __name__ == "__main__":
    findings = parse_log_file("Week2/input_files/mcu_log.txt")
    if findings:
        print("Attention!!!!! The programme has warnings:")
        for f in findings:
            print(f) 
    else:
        print("No assertation found!")