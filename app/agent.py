# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import datetime
import os
from zoneinfo import ZoneInfo

import google.auth
from google.adk.agents import Agent
from google.adk.apps.app import App

_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"


# 2. 도구(Tool) 정의: HWP -> PDF 변환
# 기존 함수를 지우고 이걸로 교체하세요
def convert_hwp_to_pdf(file_path: str) -> str:
    """
    HWP 파일을 PDF로 변환하고 텍스트를 추출하는 시뮬레이션 도구입니다.
    실제 변환 엔진이 없으므로, 테스트를 위해 가상의 문서 내용을 반환합니다.
    """
    print(f"[System] Processing HWP file: {file_path}")
    
    # [시뮬레이션] 마치 HWP 파일 안에 이런 내용이 들어있었다고 가정하고 텍스트를 리턴합니다.
    # 실제 개발 시에는 여기서 LibreOffice로 변환된 PDF의 텍스트를 OCR/Parsing해서 리턴해야 합니다.
    mock_content = """
    [문서 제목: 2025년도 1분기 에이전트 개발 보고서]
    
    1. 개요
       본 문서는 Google Cloud 기반의 HWP 변환 에이전트 개발 현황을 공유함.
    
    2. 주요 성과
       | 구분 | 목표 | 달성률 | 비고 |
       |---|---|---|---|
       | 인프라 구축 | 100% | 100% | Terraform 활용 |
       | 에이전트 연동 | 90% | 100% | Vertex AI 적용 |
       | HWP 파싱 | 80% | 50% | 모듈 개발 중 |
       
    3. 향후 계획
       - 2분기 내 정식 서비스 배포 예정
       - 보안 모듈(PII 마스킹) 추가 도입
    """
    
    return mock_content


hwp_agent = Agent(
    name="hwp_agent",
    model="gemini-3-pro-preview",
    instruction="""
    **Role:**
    You are a document processing assistant.
    
    **Workflow:**
    1. When a user uploads an HWP file, call the `convert_hwp_to_pdf` tool.
    2. The tool will return the **extracted text content** of the document.
    3. Analyze this content and convert it into **JSON format**.
    
    **Constraint:**
    - The JSON must capture the 'Title', 'Sections', and 'Tables' clearly.
    - If there is a table in the text, structure it as a list of objects in JSON.
    """,
    tools=[convert_hwp_to_pdf],
    description="HWP 파일을 받아 PDF로 변환 후 구조화된 데이터(JSON/Markdown)로 추출하는 에이전트"
)

app = App(root_agent=hwp_agent, name="app")
