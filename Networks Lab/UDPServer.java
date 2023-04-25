import java.net.*;

public class UDPServer {
    public static void main(String[] args) throws Exception {
        DatagramSocket server = new DatagramSocket(8080);
        while (true) {
            byte[] b = new byte[1024];
            DatagramPacket p = new DatagramPacket(b, b.length);
            server.receive(p);
            String[] nums = new String(p.getData(), 0, p.getLength()).split(" ");
            int r = Integer.parseInt(nums[0]) + Integer.parseInt(nums[1]);
            server.send(new DatagramPacket(Integer.toString(r).getBytes(), Integer.toString(r).getBytes().length,
                    p.getAddress(), p.getPort()));
            System.out.println("Result: " + r);
        }
    }
}
