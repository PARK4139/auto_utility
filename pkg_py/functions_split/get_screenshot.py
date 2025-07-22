def get_screenshot():
    import inspect
    import numpy as np
    import pyautogui
    func_n = inspect.currentframe().f_code.co_name
    # 화면 캡처 (PyAutoGUI를 사용)
    screenshot = pyautogui.screenshot()
    # PIL 이미지를 OpenCV 이미지로 변환
    open_cv_image = np.array(screenshot)
    # RGB → BGR 색상 변환 (OpenCV는 BGR 형식 사용)
    import cv2
    open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
    return open_cv_image
