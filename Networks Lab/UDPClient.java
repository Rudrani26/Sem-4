import java.net.*;
import java.util.Scanner;

public class UDPClient {
    public static void main(String[] args) throws Exception {
        DatagramSocket client = new DatagramSocket();
        InetAddress serverAddress = InetAddress.getByName("localhost");
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Enter two numbers: ");
            String input = scanner.nextLine();
            byte[] b = input.getBytes();
            client.send(new DatagramPacket(b, b.length, serverAddress, 8080));
            DatagramPacket p = new DatagramPacket(new byte[1024], 1024);
            client.receive(p);
            System.out.println("Result: " + new String(p.getData(), 0, p.getLength()));
        }
    }
}
