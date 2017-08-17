package rpc;

import java.net.InetSocketAddress;

/**
 * RPC 测试程序 <br>
 * 		1、启动监听服务 <br>
 * 		2、创建客户端，并连接服务器 <br>
 * @author kaiLee
 *
 */
public class RpcTest {
	
	public static void main(String[] args ) {
		
		String hostname = "localhost";
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
		
		RpcImporter<EchoService> importer = new RpcImporter<EchoService>();
		EchoService	echo = importer.importer(EchoServiceImpl.class, new InetSocketAddress(hostname, port) );
		System.out.println( echo.echo("Are you ok ?") );
	}
}
