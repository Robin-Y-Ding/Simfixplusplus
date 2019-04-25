package cofix.core.parser.search;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

import org.eclipse.jdt.core.dom.CompilationUnit;

import cofix.common.util.JavaFile;
import cofix.core.parser.search.SimpleFilter.CollectorVisitor;

public class Test {
	public static void main(String[] args) throws IOException {
		String file = "/home/joe/ChartFrame.java";
		CompilationUnit unit = JavaFile.genASTFromFile(file);
		System.out.println(unit);
	}
}
