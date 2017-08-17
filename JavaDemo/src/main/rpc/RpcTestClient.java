package rpc;

import java.net.InetSocketAddress;

/**
 * Rpc 客户端测试程序 <br>
 * 先启动Rpc服务器程序
 * @author kaiLee
 *
 */
public class RpcTestClient {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String hostname = "localhost";
		int	   port = 8888;
		
		RpcImporter<EchoService> importer = new RpcImporter<EchoService>();
		EchoService	echo = importer.importer(EchoServiceImpl.class, new InetSocketAddress(hostname, port) );
		System.out.println( echo.echo("Are you ok ?") );
	}
}
