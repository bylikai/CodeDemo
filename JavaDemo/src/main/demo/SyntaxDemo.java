package demo;


/**
 * 语法测试
 * @author kaiLee
 *
 */
public class SyntaxDemo {
	private States state = States.NOT_CONNECTED;
	
	public String conLossPacket() {
		String str = "";
        switch (state) {
        case AUTH_FAILED:
            str = "AUTHFAILED";
            break;
        case CLOSED:
            str = "SESSIONEXPIRED";
            break;
        default:
            str = "CONNECTIONLOSS";
        }
       
        return str;
    }
	
	public enum States {
        CONNECTING, ASSOCIATING, CONNECTED, CONNECTEDREADONLY,
        CLOSED, AUTH_FAILED, NOT_CONNECTED;

        public boolean isAlive() {
            return this != CLOSED && this != AUTH_FAILED;
        }

        /**
         * Returns whether we are connected to a server (which
         * could possibly be read-only, if this client is allowed
         * to go to read-only mode)
         * */
        public boolean isConnected() {
            return this == CONNECTED || this == CONNECTEDREADONLY;
        }
    }
}
