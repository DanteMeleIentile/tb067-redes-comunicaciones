import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Sumar(self, request, context):
        resultado = request.a + request.b
        print(f"Servidor: Recibí pedido para sumar {request.a} + {request.b}. Resultado: {resultado}")
        return calculator_pb2.SumarResponse(resultado=resultado)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051') 
    print("Servidor gRPC iniciado en el puerto 50051. Esperando peticiones...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()