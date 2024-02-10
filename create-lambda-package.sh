rm my_lambda_function.zip && \
cd backend/venv/lib/python3.10/site-packages && \
zip -r ../../../../my_lambda_function.zip . && \
cd ../../../.. && \
zip -g my_lambda_function.zip lambda_function.py && \
zip -g my_lambda_function.zip db.py && \


mv my_lambda_function.zip ../