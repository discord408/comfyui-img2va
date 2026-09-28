import runpod

# RunPod 서버리스가 요구하는 기본 핸들러 함수 구조
def handler(job):
    job_input = job.get("input", {})
    # 여기서 ComfyUI API를 호출하거나 작업을 처리하는 로직이 들어갑니다.
    # worker-comfyui 내부 구조에 따라 기본 핸들러 함수를 임포트해서 쓸 수도 있습니다.
    return {"status": "success"}

runpod.serverless.start({"handler": handler})
