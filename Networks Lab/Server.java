import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) throws IOException {
        int portNumber = 8080;
        ServerSocket serverSocket = new ServerSocket(portNumber);
        System.out.println("Server started");
        while (true) {
            try (Socket clientSocket = serverSocket.accept();
                    BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                    PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {

                System.out.println("Client connected");

                String[] numbers = in.readLine().split(" ");
                int result = Integer.parseInt(numbers[0]) + Integer.parseInt(numbers[1]);
                System.out.println("Result: " + result);
                out.println(result);

            } catch (NumberFormatException | IOException e) {
                System.err.println("Error handling client request: " + e.getMessage());
            }
        }
    }
}
