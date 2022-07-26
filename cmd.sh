# 准备credentials
# cn-northwest-1
python3 -m venv .venv && source .venv/bin/activate # 初始化一个虚拟环境，

pip install seed-farmer==0.1.0
pip install aws-codeseeder==0.3.1

python3 patch/seedfarmer_cn_fix.py

export AWS_ACCESS_KEY_ID=XXX
export AWS_SECRET_ACCESS_KEY=XXX
export AWS_REGION=cn-northwest-1
export AWS_DEFAULT_REGION=cn-northwest-1

# 有可能需要cdk bootstrap一下，如果从来没有报过cdk的话
codeseeder deploy seedkit exampleproj # 部署codeseeder工具包

cd exampleproject/
seedfarmer apply manifests/examples/deployment.yaml # 如果codeseeder的seedkit没有部署的话，这时候会先部署对应的seedkit，然后才会部署module
