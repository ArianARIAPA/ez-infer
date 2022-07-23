def test_imports():
    from ezinfer.onnx_infer import OnnxInfer
    from ezinfer.pytorch_infer import PytorchInfer
    from ezinfer.tensorflow_infer import TensorflowInfer
    from ezinfer.mxnet_infer import MxnetInfer
    assert 1 == 1
