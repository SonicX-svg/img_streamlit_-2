"""test_main.py"""

from steamlit.testing.v1 import AppTest

def test_increment_and_add():
   at = AppTest.from_file('main.py').run()
   at = at.file_uploader[0].set_value('''https://storage.googleapis.com/kagglesdsdata/datasets/1786300/2914256/train_transformed/cat108.jpg?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20240123%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20240123T172115Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=22dc15c2959fbdcc3b59cc5650099774d605f6cd4b012a08ca7ef4e9361d71e4d8ccedb88366acd90287b03dec3d53fbf1e7caacda9bf75b3eac05f6c84e9db6021d02335b0955c8cf9b00a93ebb7f9bd58112f99eda5d8093d91fd933876ca57494837b0e205fc257e98012e01927ae14217d32162d2c0d023bdaf6f49de2d4bb5dc3268131ad94097575bda1968e60b5658804393801aa0e24254e14ee7b5d4cb4eab7f98737ceaca02221772bf070f769902f746d45864fd2780a2d8bdf36e8add1c7de2bec2ac10a920818e8ce81275c83339aee76672dce1f72ba4c11d8e88a5d962046c13479faa7f331148a11274ede92503f4cb99e6c9b9840e874fc''')


   
