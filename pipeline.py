from backend.services.contract_service import ContractAnalysisService

_service = None


def get_service(api_key):
    global _service

    if _service is None:
        _service = ContractAnalysisService(api_key)

    return _service


def run_pipeline(uploaded_file, api_key):

    service = get_service(api_key)

    return service.analyze(uploaded_file)