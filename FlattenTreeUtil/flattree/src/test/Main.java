package test;

import com.github.gumtreediff.gen.Generators;
import com.github.gumtreediff.tree.ITree;
import com.github.gumtreediff.tree.Tree;
import com.github.gumtreediff.client.Run;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Stack;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new FileReader("C:\\Users\\huang\\Desktop\\validnext.tree.txt"));
    	try {
    	    StringBuilder sb = new StringBuilder();
    	    String line = br.readLine();

    	    while (line != null) {
    	    	ITree root = createTreeFromTreeString(line);
    	    	System.out.println(root.toTreeString());
    	    	String res = printTree(root, "");
    	        sb.append(res);
    	        sb.append(System.lineSeparator());
    	        line = br.readLine();
    	    }
    	    String everything = sb.toString();
    	    // PrintStream fileOut = new PrintStream("C:\\\\Users\\\\huang\\\\Desktop\\\\valid_next.txt");
    	    // System.setOut(fileOut);
    	    //System.out.println(everything);
    	} finally {
    	    br.close();
    	}
    	
    }

    public static String printTree(ITree root, String s) {
    	s += "{";
    	
    	List temp = Arrays.asList(root.toShortString().split("@@"));
    	if(temp.size() > 1) s += temp.get(temp.size() - 1);
    	for(ITree child : root.getChildren()) {
    		s = printTree(child,s);
    	}
    	s += "}";
    	return s;
    }
    
    public static String reFormatTreeStr(String treeStr){
        StringBuffer buffer = new StringBuffer();
        for (int i = 0; i < treeStr.length(); i++) {
            char ch = treeStr.charAt(i);
            if (ch == '(') {
                if ((i == 0) || (treeStr.charAt(i - 1) != '=')) {
                    buffer.append("` ");
                }
                else if (treeStr.charAt(i + 1) == ')') {
                    i++;
                    buffer.append("()");
                }
                else {
                    buffer.append("(");
                }
            }
            else if (ch == ')') {
                if (treeStr.charAt(i - 1) != '=') {
                    buffer.append(" ``");
                } else {
                    buffer.append(")");
                }
            }
            else {
                buffer.append(treeStr.charAt(i));
            }
        }
        treeStr = buffer.toString();
        String[] parts = treeStr.split(" ");
        buffer = new StringBuffer();
        String[] arrayOfString1;
        int j = (arrayOfString1 = parts).length;
        for (int i = 0; i < j; i++) {
            String part = arrayOfString1[i];
            if (part.contains("{val=")) {
                part = part.substring(0, part.length() - 1);
                int bidx = part.indexOf("{val=");
                String beforePart = part.substring(0, bidx);
                String afterPart = part.substring(bidx + 5);
                buffer.append(beforePart);
                buffer.append(" ` ");
                buffer.append(afterPart);
                buffer.append(" `` ");
            }
            else{
                buffer.append(part);
                buffer.append(" ");
            }
        }
        treeStr = buffer.toString();
        return treeStr;
    }



    private static void fixGeneratedTree(ITree root) {
        List<ITree> children = root.getChildren();
        if (root.isLeaf()) {
            return;
        }
        if ((children.size() == 1) && (((ITree)children.get(0)).getType() == -58989)) {
            root.setLabel(((ITree)children.get(0)).getLabel());
            root.setChildren(new ArrayList<>());
        }
        else {
            for (ITree child : children) {
                fixGeneratedTree(child);
            }
        }
    }

    public static ITree createTreeFromTreeString(String tstr) {
        String treeStr = reFormatTreeStr(tstr);
        String[] tokens = treeStr.trim().split(" ");
        Stack<Object> st = new Stack<Object>();
        String[] arrayOfString1;
        int j = (arrayOfString1 = tokens).length;
        for (int i = 0; i < j; i++) {
            String token = arrayOfString1[i];
            token = token.trim();
            if (token.length() != 0) {
                if (token.compareTo("`") == 0) {
                    st.push(token);
                }
                else if (token.compareTo("``") == 0) {
                    List<Object> children = new ArrayList<Object>();
                    Object topOfStack = st.pop();
                    String topStackStr = "";
                    if ((topOfStack instanceof ITree)) {
                        topStackStr = ((ITree)topOfStack).toShortString();
                    } else {
                        topStackStr = topOfStack.toString();
                    }
                    while (topStackStr.compareTo("`") != 0) {
                        children.add(topOfStack);
                        topOfStack = st.pop();
                        if ((topOfStack instanceof ITree)) {
                            topStackStr = ((ITree)topOfStack).toShortString();
                        } else {
                            topStackStr = topOfStack.toString();
                        }
                    }
                    if (st.isEmpty()) {
                        st.push(children.get(0));
                    }
                    else {
                        topOfStack = st.pop();
                        ITree tree = (ITree)topOfStack;
                        for (Object child : children) {
                            ITree ch = (ITree)child;
                            ch.setParent(tree);
                            tree.addChild(ch);
                        }
                        st.push(tree);
                    }
                }
                else{
                    String label = token;
                    int type = -58989;
                    try {
                        type = Integer.parseInt(token);
                        label = "";
                    }
                    catch (NumberFormatException localNumberFormatException) {
                    }
                    ITree node = new Tree(type, label);
                    st.push(node);
                }
            }
        }
        ITree root = (ITree)st.pop();
        fixGeneratedTree(root);
        return root;
    }
}