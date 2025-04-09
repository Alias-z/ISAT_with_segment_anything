# -*- coding: utf-8 -*-
# @Author  : LG

import sys
print("Debug: Imported sys")
from ISAT.main import main
print("Debug: Imported main function from ISAT.main")

if __name__ == '__main__':
    print("Debug: Starting application")
    try:
        main()
        print("Debug: Application completed successfully")
    except Exception as e:
        print(f"Debug: Error in main: {e}")
        import traceback
        traceback.print_exc()