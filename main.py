import os
import sys
from agent_system import AgentSystem

def main():
    """主程式入口"""
    try:
        # 初始化代理系統
        agent = AgentSystem()
        
        # 啟動代理系統
        agent.start()
        
        print("Stock AI Agent 已啟動")
        print("等待指令...")
        
        # 保持程式運行
        while True:
            try:
                # 可以在這裡添加用戶輸入處理
                pass
            except KeyboardInterrupt:
                print("\n正在關閉代理系統...")
                agent.stop()
                break
                
    except Exception as e:
        print(f"啟動失敗: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
