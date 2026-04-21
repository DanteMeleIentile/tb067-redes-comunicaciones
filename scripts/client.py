import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    print("Cliente: Intentando conectar al servidor...")
    with grpc.insecure_channel('localhost:50051') as channel:
    #with grpc.insecure_channel('10.185.21.49:50051') as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Sumar(calculator_pb2.SumarRequest(a=10, b=5))
    print(f"Cliente: El servidor respondió que el resultado es {response.resultado}")

if __name__ == '__main__':
    run()