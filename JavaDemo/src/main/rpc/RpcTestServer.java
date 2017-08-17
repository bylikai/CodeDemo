package rpc;

/**
 * Rpc服务器程序
 * @author kaiLee
 *
 */
public class RpcTestServer {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String hostname = "0.0.0.0";
		int	   port = 8888;
		
		//1.启动服务监听 8888端口
		Thread t = new Thread( new Runnable() {
			
			@Override
			public void run() {
				// TODO Auto-generated method stub
				try {
					RpcExporter.exporter( hostname, port );
				}
				catch( Exception e ) {
					e.printStackTrace();
				}
			}
		});
		t.start();
	}

}
