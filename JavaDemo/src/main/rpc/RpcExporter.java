package rpc;

import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.Method;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.Executor;
import java.util.concurrent.Executors;

/**
 * 服务发布者：<br>
 * 		1、作为服务端，监听客户端的TCP连接，接收到新的客户端连接之后，将其封装成Task，由线程池执行<br>
 * 		2、将客户端发送过来的码流反序列化成对象，反射调用服务实现者，获取执行结果<br>
 * 		3、将执行结果对象发序列化，通过Socket发送给客户端<br>
 * 		4、远程调用完成之后，释放客户端Socket等连接资源，防止句柄泄漏
 * @author kaiLee
 *
 */
public class RpcExporter {
	/**
	 * 线程池：用于执行监听客户端连接服务
	 */
	private static Executor executor = Executors.newFixedThreadPool( 
			Runtime.getRuntime().availableProcessors() );
	
	public static void exporter( String hostname, int port ) throws Exception {
		
		ServerSocket	server = new ServerSocket();
		server.bind( new InetSocketAddress(hostname, port));
		
		try {
			while(true) {
				executor.execute( new ExporterTask( server.accept() ));
			}
		}
		finally {
			server.close();
		}
	}
	
	
	private static class ExporterTask implements Runnable {
		private Socket	client = null;
		
		public ExporterTask(Socket client) {
			this.client = client;
		}
		
		@Override
		public void run() {
			ObjectInputStream	input = null;
			ObjectOutputStream	output= null;
			try {
				
				//1.获取客户端输入，输出流
				input =  new ObjectInputStream( client.getInputStream() );
				
				
				//2.从输入流读取interfaceName, methodName, parameterName, arguments
				String interfaceName 	= input.readUTF();
				String methodName 		= input.readUTF();
				Class<?>[] parameterTypes= (Class<?>[])input.readObject();
				Object[] arguments		= (Object[])input.readObject();
				
				//3.通过interfaceName获取服务, 通过methodName和parameterTypes获取方法，通过arguments获取结果result
				Class<?> service 		= Class.forName(interfaceName);
				Method	 method			= service.getMethod(methodName, parameterTypes);
				Object	 result			= method.invoke(service.newInstance(), arguments);
				
				output = new ObjectOutputStream( client.getOutputStream() );
				
				//4.将结果反序列化写入输出流
				output.writeObject(result);
				
			}
			catch( Exception e ) {
				e.printStackTrace();
			}
			finally {
				// 关闭输出流
				if( null != output ) {
					try {
						output.close();
					}
					catch( Exception e ) {
						e.printStackTrace();
					}
				}
				
				// 关闭输入流
				if( null != input ) {
					try {
						input.close();
					}
					catch( Exception e ) {
						e.printStackTrace();
					}
				}
				
				// 关闭客户端socket: 
				if( null != client ) {
					try {
						client.close();
					}
					catch( Exception e ) {
						e.printStackTrace();
					}
				}
			}
		}
	}
}
