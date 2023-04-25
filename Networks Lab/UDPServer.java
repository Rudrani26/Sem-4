import java.net.*;

public class UDPServer {
    public static void main(String[] args) throws Exception {
        DatagramSocket serverSocket = new DatagramSocket(8080);
        System.out.println("Server started");

        while (true) {
            byte[] buffer = new byte[1024];
            DatagramPacket receivePacket = new DatagramPacket(buffer, buffer.length);
            serverSocket.receive(receivePacket);
            String input = new String(receivePacket.getData(), 0, receivePacket.getLength());
            String[] numbers = input.split(" ");
            int result = Integer.parseInt(numbers[0]) + Integer.parseInt(numbers[1]);
            System.out.println("Result: " + result);

            byte[] sendData = Integer.toString(result).getBytes();
            DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, receivePacket.getAddress(),
                    receivePacket.getPort());
            serverSocket.send(sendPacket);
        }
    }
}
