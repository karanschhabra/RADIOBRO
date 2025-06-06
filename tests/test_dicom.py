import pydicom
from pydicom.data import get_testdata_file

def test_dicom_loading():
    filename = get_testdata_file("CT_small.dcm")
    ds = pydicom.dcmread(filename)
    assert ds.PatientName is not None

