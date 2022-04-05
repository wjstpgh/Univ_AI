# Univ_AI
AI basic study

## Constraint satisfaction problems(CSPs)
are defined with a set of variables or objects whose state must satisfy a number of constraints. CSPs represent the entities in a problem as a homogeneous collection of finite constraints over variables, which is solved by constraint satisfaction algorithms.


* 8-Queen

rows = a / columns = b / U = Universal(set) / S = Solution(set)

U = A[a][b] where a ∈ [1, 8] and b ∈ [1, 8]

S = A[rows][columns] where

A[rows][1] != A[rows][2] != A[rows][3] != … != A[rows][8]

AND

A[1][columns] != A[2][columns] != A[3][columns] != … != A[8][columns]

AND

A[rows][columns] ∈ !A[rows++][columns++] and !A[rows--][columns--] 


* Sudoku

X = {a[0][0],a[0][1],a[0][2],......a[4][4],.....a[8][8]}

D = {1,2...9}

C1 = {a[row][0]!=a[row][1]!=a[row][2].....!=a[row][9]}

C2 = {a[0][column]!=a[1][column]!=......a[9][column]}

C3 = {i,j={0,3,6}|a[i][j]!=a[i+1][j]!=...a[i+2][j+2]}


* 4Color problem

X = {a[0][0],a[0][1],a[0][2],......a[4][4],.....a[8][8]}

D = {1,2...9}

C1 = {a[row][0]!=a[row][1]!=a[row][2].....!=a[row][9]}

C2 = {a[0][column]!=a[1][column]!=......a[9][column]}

C3 = {i,j={0,3,6}|a[i][j]!=a[i+1][j]!=...a[i+2][j+2]}


## Graph coloring problems and applications
were taught in the previous lecture. As we discussed, graph coloring is widely used. But, there is no efficient algorithm available for coloring a graph with minimum number of colors as the problem is a known NP-complete problem. There are approximate algorithms to solve the graph coloring problem.

> We have many problem(P) that is NP-group, and one standard(Q) is difficult to solve problem that is NP-hard. One of problem contain both NP-group and NP-hard that is NP-complete.

* Given the Korea administrative region map(Figure 1), convert the map into a graph.

![image](https://user-images.githubusercontent.com/26988563/161731866-649390ef-1c4a-4918-83c1-3a76558ad0d2.png)

* Find the minimum number of colors for the Korea map.
	• Design in pseudo code.
  
```
a[0]=first color;
for(int i=0;i<nod_num;i++){
	if (not been used on any previously colored vertices){
		a[i]=most low number color;
	}
	if(all previously used colors appear on vertuces adjacent to nod){
		a[nod]=new color;
	}
}
```

* Implement your algorithm to find the minimum number of colors.

code
```
package map_color;

import java.util.Arrays;
import java.util.Iterator;

public class TestGraph {
	static String arr[]= {"0인천","1경기", "2강원", "3독도", "4충남", "5충북", "6대전", 
	"7경북", "8전북", "9대구", "10광주", "11경남", "12울산", "13전남", "14부산", "15제주"};

	public static void main(String[] args) {
	// TODO Auto-generated method stub
	System.out.println("---Greedy Algorithm---");
	Graph g = new Graph(16);
	
	System.out.println("Graph:");
	
	g.addEdge(0, 1);
	g.addEdge(1, 2);
	g.addEdge(1, 4);
	g.addEdge(1, 5);
	g.addEdge(2, 7);
	g.addEdge(4, 5);
	g.addEdge(4, 6);
	g.addEdge(5, 6);
	g.addEdge(5, 7);
	g.addEdge(7, 9);
	g.addEdge(8, 11);
	g.addEdge(8, 13);
	g.addEdge(9, 11);
	g.addEdge(10, 13);
	g.addEdge(11, 12);
	g.addEdge(11, 13);
	g.addEdge(11, 14);
	g.addEdge(12, 14);
	
	g.printGraph();
	
	greedyColoring(g);
	
	System.out.println("--------------------------");
	}

	public static void greedyColoring(Graph g) {
	int V = g.getvCount();
	
	int colors[] = new int[V];
	
	Arrays.fill(colors, -1);
	
	colors[0] = 0;
	
	boolean available[] = new boolean[V];
	
	Arrays.fill(available, true);
	
	for(int u=1; u<V;u++) {
	Iterator<Integer> it = g.neighbors(u).iterator();
	while(it.hasNext()) {
	int i=it.next();
	if(colors[i]!=-1) {
	available[colors[i]]=false;
	}
	}
	
	int cr;
	for(cr=0; cr<V;cr++) {
	if(available[cr])
	break;
	}
	
	colors[u] = cr;
	
	Arrays.fill(available, true);
	}
	
	printColors(colors);
	}
	
	public static boolean isSafe(int v, Graph g, int colors[], int cr) {
	for(int i=0;i<g.getvCount();i++) {
	if(g.hasEdge(v, i)&&cr==colors[i]) {
	return false;
	}
	}
	return true;
	}
	
	public static boolean graphColoringUtil(Graph g, int m, int colors[], int v) {
	if(v==g.getvCount())
	return true;
	
	for(int cr=1;cr<=m;cr++) {
	if(isSafe(v,g,colors,cr)) {
	if(graphColoringUtil(g, m, colors, v+1))
	return true;
	
	colors[v] =0;
	}
	}
	
	return false;
	}
	
	
	public static void printColors(int[] colors) {
	String col[] = {"RED", "BLUE", "GREEN", "YELLOW"}; 
	for(int i=0;i<colors.length;i++) 
	System.out.println(arr[i]+" --> Color "+col[colors[i]]);
	}
}
```

Graph.java
```
package map_color;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class Graph {
	private int vCount;
	private List<Integer>[] adj;
	
	public int getvCount() {
	return vCount;
	}
	
	public Graph(int vCount) {
	this.vCount = vCount;
	adj = (List<Integer>[])new List[vCount];
	for(int i=0; i<vCount;i++)
	adj[i] = new ArrayList<Integer>();
	}
	
	public void addEdge(int i, int j) {
	adj[i].add(j);
	adj[j].add(i);
	}
	
	public void removeEdge(int i, int j) {
	Iterator<Integer> it = adj[i].iterator();
	while(it.hasNext()) {
	if(it.next()==j) {
	it.remove();
	return;
	}
	}
	}
	
	public boolean hasEdge(int i, int j) {
	return adj[i].contains(j);
	}
	
	public List<Integer> neighbors(int vertex){
	return adj[vertex];
	}
	
	public void printGraph() {
	for (int i=0; i<vCount;i++) {
	List<Integer> edges= neighbors(i);
	System.out.print(i+": ");
	for(int j=0;j<edges.size();j++) {
	System.out.print(edges.get(j)+" ");
	}
	System.out.println();
	}
	}

}
```

* Result

![image](https://user-images.githubusercontent.com/26988563/161731917-0c95dbbb-89dc-43a1-bcad-35073eb1114c.png)

* Discuss about how to analyze the space and time complexity of your own
	  algorithm.
    
> Space complexity :: The spatial complexity of this algorithm can be calculated by adding together the variables, arguments, and sets created for the constraints for the CSP.

> Time complexity ::　The time complexity of the algorithm can be estimated by multiplying the number of branches searching for a possibility for the search by the number of functions operating for that search.

![image](https://user-images.githubusercontent.com/26988563/161731928-a2a08be9-59b9-4920-b166-1b890d30aeb1.png)

* Report the order of the vertices encountered on a breadth-first search starting from vertex A. Choose the vertices in alphabetical order.

A->B->E->F->G->J->K->O->P->U->V->W->N->M->I->Y->L->H->S->T->X->D->Q

* Report the order of the vertices encountered on a depth-first search starting from vertex A. Choose the vertices in alphabetical order.

A->B->N->E->F->M->S->D->Q->T->H->L->K->P->I->Y->W->X->G->U->O->J->V


## The edge weight
is distance between two nodes and the weight below a node is the cost to node G.

![image](https://user-images.githubusercontent.com/26988563/161731942-7744f62b-2fd1-4bc4-b27a-7fb689f1e787.png)

* When we start at node A and ignore the given cost values, find the breadth-first search of the graph.

![image](https://user-images.githubusercontent.com/26988563/161731953-0f839aad-5e0a-4b82-a165-07a1e065eb7b.png)

* When we start at node A and ignore the given cost values, give the depth-first search of the graph.

![image](https://user-images.githubusercontent.com/26988563/161731958-07aad5e3-e52a-49a0-ae71-c96c852354d7.png)

* Find the optimal solution from A to G by applying the A∗ algorithm.

![image](https://user-images.githubusercontent.com/26988563/161731966-d0ea4197-3122-408b-9dc1-cf8efdd34ea3.png)

#### For any event x and y in a sample space, prove

P(x|y)P(y) = P(y|x)P(x).

(1)P(x|y) = P(x, y) / P(y) 

=> P(x, y) = P(x|y)P(y)

(2)P(y|x) = P(x, y) / P(x) 

=> P(x, y) = P(x|y)P(x)

∴ P(x|y)P(y) = P(y|x)P(x)

## Compute
Given the discrete probability distribution in Table 1

![image](https://user-images.githubusercontent.com/26988563/161731983-57b31d65-832b-4aac-846d-9296b93df3c6.png)

* P(W)

<html xmlns="http://www.w3.org/TR/REC-html40" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"><head><!--[if !mso]>
<style>
v\:* {behavior:url(#default#vml);}
o\:* {behavior:url(#default#vml);}
w\:* {behavior:url(#default#vml);}
.shape {behavior:url(#default#vml);}
</style>
<![endif]
--><!--p.0
{mso-style-name:"바탕글";line-height:160%;margin-left:0pt;margin-right:0pt;text-indent:0pt;margin-top:0pt;margin-bottom:0pt;text-align:justify;word-break:break-hangul;layout-grid-mode:both;vertical-align:baseline;mso-pagination:none;text-autospace:none;mso-padding-alt:0pt 0pt 0pt 0pt;mso-ascii-font-family:함초롬바탕;mso-ascii-font-family:함초롬바탕;mso-font-width:100%;letter-spacing:0pt;mso-text-raise:0pt;font-size:10.0pt;color:#000000;mso-font-kerning:0pt;}
--></head><body><!--StartFragment-->

W | P
-- | --
Sun | 0.6
Rain | 0.4

<!--EndFragment--></body></html>

***

* P(W|S = winter)

<html xmlns="http://www.w3.org/TR/REC-html40" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"><head><!--[if !mso]>
<style>
v\:* {behavior:url(#default#vml);}
o\:* {behavior:url(#default#vml);}
w\:* {behavior:url(#default#vml);}
.shape {behavior:url(#default#vml);}
</style>
<![endif]
--><!--p.0
{mso-style-name:"바탕글";line-height:160%;margin-left:0pt;margin-right:0pt;text-indent:0pt;margin-top:0pt;margin-bottom:0pt;text-align:justify;word-break:break-hangul;layout-grid-mode:both;vertical-align:baseline;mso-pagination:none;text-autospace:none;mso-padding-alt:0pt 0pt 0pt 0pt;mso-ascii-font-family:함초롬바탕;mso-ascii-font-family:함초롬바탕;mso-font-width:100%;letter-spacing:0pt;mso-text-raise:0pt;font-size:10.0pt;color:#000000;mso-font-kerning:0pt;}
--></head><body><!--StartFragment-->

W | P
-- | --
Sun | 0.15
Rain | 0.25

<!--EndFragment--></body></html>

normalization(0.4)

<html xmlns="http://www.w3.org/TR/REC-html40" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"><head><!--[if !mso]>
<style>
v\:* {behavior:url(#default#vml);}
o\:* {behavior:url(#default#vml);}
w\:* {behavior:url(#default#vml);}
.shape {behavior:url(#default#vml);}
</style>
<![endif]
--><!--p.0
{mso-style-name:"바탕글";line-height:160%;margin-left:0pt;margin-right:0pt;text-indent:0pt;margin-top:0pt;margin-bottom:0pt;text-align:justify;word-break:break-hangul;layout-grid-mode:both;vertical-align:baseline;mso-pagination:none;text-autospace:none;mso-padding-alt:0pt 0pt 0pt 0pt;mso-ascii-font-family:함초롬바탕;mso-ascii-font-family:함초롬바탕;mso-font-width:100%;letter-spacing:0pt;mso-text-raise:0pt;font-size:10.0pt;color:#000000;mso-font-kerning:0pt;}
--></head><body><!--StartFragment-->

W | P
-- | --
Sun | 0.375
Rain | 0.625

<!--EndFragment--></body></html>

***

* P(W|S = winter, T = cold)

<html xmlns="http://www.w3.org/TR/REC-html40" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"><head><!--[if !mso]>
<style>
v\:* {behavior:url(#default#vml);}
o\:* {behavior:url(#default#vml);}
w\:* {behavior:url(#default#vml);}
.shape {behavior:url(#default#vml);}
</style>
<![endif]
--><!--p.0
{mso-style-name:"바탕글";line-height:160%;margin-left:0pt;margin-right:0pt;text-indent:0pt;margin-top:0pt;margin-bottom:0pt;text-align:justify;word-break:break-hangul;layout-grid-mode:both;vertical-align:baseline;mso-pagination:none;text-autospace:none;mso-padding-alt:0pt 0pt 0pt 0pt;mso-ascii-font-family:함초롬바탕;mso-ascii-font-family:함초롬바탕;mso-font-width:100%;letter-spacing:0pt;mso-text-raise:0pt;font-size:10.0pt;color:#000000;mso-font-kerning:0pt;}
--></head><body><!--StartFragment-->

W | P
-- | --
Sun | 0.1
Rain | 0.2

<!--EndFragment--></body></html>

normalization(0.3)

<html xmlns="http://www.w3.org/TR/REC-html40" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"><head><!--[if !mso]>
<style>
v\:* {behavior:url(#default#vml);}
o\:* {behavior:url(#default#vml);}
w\:* {behavior:url(#default#vml);}
.shape {behavior:url(#default#vml);}
</style>
<![endif]
--><!--p.0
{mso-style-name:"바탕글";line-height:160%;margin-left:0pt;margin-right:0pt;text-indent:0pt;margin-top:0pt;margin-bottom:0pt;text-align:justify;word-break:break-hangul;layout-grid-mode:both;vertical-align:baseline;mso-pagination:none;text-autospace:none;mso-padding-alt:0pt 0pt 0pt 0pt;mso-ascii-font-family:함초롬바탕;mso-ascii-font-family:함초롬바탕;mso-font-width:100%;letter-spacing:0pt;mso-text-raise:0pt;font-size:10.0pt;color:#000000;mso-font-kerning:0pt;}
--></head><body><!--StartFragment-->

W | P
-- | --
Sun | 0.333..
Rain | 0.666..

<!--EndFragment--></body></html>





