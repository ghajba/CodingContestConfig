package tcptest;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

/**
 * Simple class for a TCP client used for CCC-communication.
 * 
 * @author GHajba
 *
 */
public class TCPClient {

    /**
     * The main method with the endless loop. It reads the data from the server then sends an update.
     * 
     * @param args
     *            requires 2 parameters: server-host and server-port. Currently no validation is added for these arguments.
     * @throws IOException if the connection to the server cannot be closed when the application ends.
     */
    public static void main(String... args) throws IOException {
        Socket clientSocket = null;
        String host = args[0];
        String port = args[1];
        try {
            String serverMessage;
            clientSocket = new Socket(host, Integer.valueOf(port));
            DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
            BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            while (true) {
                while(true) {
                    serverMessage = inFromServer.readLine();
                    if("update".equals(serverMessage)) {
                        break;
                    }
                    // split and parse the server's message to use it later in the calculate method
                }
                System.out.println("FROM SERVER: " + serverMessage);
                outToServer.writeBytes(calculate(serverMessage) + '\n');
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (clientSocket != null) {
                clientSocket.close();
            }
        }
    }

    /**
     * This method should calculate the response message to send to the server.
     * @param serverInput the input provided by the server
     * @return currently an empty string
     */
    private static String calculate(String serverInput) {
        return "";
    }

}
