from datetime import datetime
from typing import Optional


class RecruitProcessLogEntity:
    def __init__(self, recruit_process_id: str, dod_id: str, process_stage: int, 
        process_status: int, process_start_time: datetime, 
        process_end_time: Optional[datetime] = None, message: Optional[str] = None, 
        recruit_process_log_id: int = 0
    ):
        self.recruit_process_id = recruit_process_id
        self.dod_id = dod_id
        self.process_stage = process_stage
        self.process_status = process_status
        self.process_start_time = process_start_time
        self.process_end_time = process_end_time
        self.message = message
        self.recruit_process_log_id = recruit_process_log_id

    def __repr__(self):
        return f"RecruitProcessLogEntity(recruit_process_id={self.recruit_process_id}, dod_id={self.dod_id}, process_stage={self.process_stage}, process_status={self.process_status}, process_start_time={self.process_start_time}, process_end_time={self.process_end_time}, message={self.message}, recruit_process_log_id={self.recruit_process_log_id})"
