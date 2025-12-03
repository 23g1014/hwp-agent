# 리소스 이름의 접두사
project_name = "hwp-agent"

# 실제 구글 클라우드 프로젝트 ID (모두 동일하게 설정)
prod_project_id        = "agent-development-kit-test"
staging_project_id     = "agent-development-kit-test"
cicd_runner_project_id = "agent-development-kit-test"

# Cloud Build에서 생성한 호스트 연결 이름
host_connection_name = "hwp-agent"

# GitHub Personal Access Token을 담을 시크릿 이름 (아래 2번 단계에서 생성함)
github_pat_secret_id = "github-pat"

# GitHub 사용자명 (URL에서 추출: 23g1014)
repository_owner = "23g1014"

# 리포지토리 이름
repository_name = "hwp-agent"

# 리전
region = "us-central1"