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

## 2-class classfication
The training set is given in Figure 1. Check out the accuracy of a training and testing sets when 80% data are used for training and the rest for testing.

![image](https://user-images.githubusercontent.com/26988563/162414837-3fcbe8ed-7ef0-48a8-8bd5-9dc9c3fa4749.png)

Build and evaluate decision trees in terms of max depth, min samples split, and min samples leaf. 

```
import pandas as pdfrom sklearn.tree import DecisionTreeClassifier import numpy as npfrom sklearn.model_selection import train_test_splitfrom sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier

df=pd.read_csv("./dstest.txt" , delimiter=',',names=["class", "x", 'y'])data=df.valuesX_train, X_test, y_train, y_test=train_test_split(data[:,1:],data[:,0],test_size=0.2, random_state=0)
print("min_sample_split_test")for i in range(200,401, 100):    dt_clf=DecisionTreeClassifier(min_samples_split=i, random_state=0)    dt_clf.fit(X_train,y_train)    pred=dt_clf.predict(X_test)    accuracy=np.mean(y_test==pred)    precision=precision_score(y_test,pred)    recall=recall_score(y_test,pred)    print("min_samples_split={0} ,accuracy=, {1:0.3f}, precsion={2:0.3f}, recall={3:0.3f}".format(i,accuracy,precision,recall))print("min_sample_leaf_test")for i in range(50,251,50):    dt_clf=DecisionTreeClassifier(min_samples_leaf=i, random_state=0)    dt_clf.fit(X_train,y_train)    pred=dt_clf.predict(X_test)    accuracy=np.mean(y_test==pred)    precision=precision_score(y_test,pred)    recall=recall_score(y_test,pred)    print("min_samples_leaf={0} ,accuracy=, {1:0.3f}, precsion={2:0.3f}, recall={3:0.3f}".format(i, accuracy, precision,recall))print("max_depth_test")for i in range(1,7,1):    dt_clf = DecisionTreeClassifier(max_depth=i, random_state=0)    dt_clf.fit(X_train, y_train)    pred = dt_clf.predict(X_test)    accuracy = np.mean(y_test == pred)    precision=precision_score(y_test,pred)    recall=recall_score(y_test,pred)    print("max_depth={0} ,accuracy=, {1:0.3f}, precsion={2:0.3f}, recall={3:0.3f}".format(i,accuracy,precision,recall))
```

* result

![image](https://user-images.githubusercontent.com/26988563/162414888-c62a64b1-49dc-47d6-934d-2f3851a96c04.png)

* Tree form

  + min_samples_split=400

![image](https://user-images.githubusercontent.com/26988563/162414901-3411f111-973b-4b2f-9e42-d55f7d0386c5.png)

  + min_samples_split=300

![image](https://user-images.githubusercontent.com/26988563/162414911-2c439802-5d23-4d9e-bb1f-d32588a0b808.png)

  + min_samples_split=200

![image](https://user-images.githubusercontent.com/26988563/162414936-95024ac6-5320-423e-9dd6-ee66f65edc2f.png)

  + min_samples_leaf=50

![image](https://user-images.githubusercontent.com/26988563/162414952-1bb1db73-d95b-4c8e-a0c6-acdb1320b207.png)

  + min_samples_leaf=100
  
![image](https://user-images.githubusercontent.com/26988563/162414971-af2bd938-5a85-4146-931d-2e3087d9d22e.png)

  + min_samples_leaf=150

![image](https://user-images.githubusercontent.com/26988563/162415007-c10748e3-7e48-4f80-94da-4528813753ff.png)

  + min_samples_leaf=200

![image](https://user-images.githubusercontent.com/26988563/162415025-443ec1e8-3ffa-4507-a084-04651cebb8b4.png)

  + min_samples_leaf=250

![image](https://user-images.githubusercontent.com/26988563/162415044-c059a8ba-5963-43ad-950c-50c275110de8.png)

  + max_deapth=1

![image](https://user-images.githubusercontent.com/26988563/162415060-142b99c8-58b2-44e9-9f33-da06de622cf0.png)

  + max_depth=2

![image](https://user-images.githubusercontent.com/26988563/162415070-64bb154b-08ec-41c6-9042-8a45e5b7015c.png)

  + max_depth=3

![image](https://user-images.githubusercontent.com/26988563/162415089-32c3ecf2-08fb-4a26-94f8-d049b709a1f3.png)

  + max_depth=4

![image](https://user-images.githubusercontent.com/26988563/162415110-6e3c7372-d865-49fe-aeb6-250b8376acbb.png)

  + max_depth=5

![image](https://user-images.githubusercontent.com/26988563/162415123-bc8fbfb5-35dc-48b7-9524-cec88c67846c.png)

  + max_depth=6

![image](https://user-images.githubusercontent.com/26988563/162415139-79969330-39b9-493c-aeb9-89827cc09806.png)



![image](https://user-images.githubusercontent.com/26988563/162415212-9d6e4d49-83e3-4946-b779-927720e5a1bf.png)
![image](https://user-images.githubusercontent.com/26988563/162415240-b4be901b-86a7-453e-bd6e-6fb773b8f12e.png)
![image](https://user-images.githubusercontent.com/26988563/162415300-aac62fa2-90e6-489a-bcf7-ff24574ec35a.png)
![image](https://user-images.githubusercontent.com/26988563/162415313-06468e3c-437a-4eb5-b743-e9e2362bf539.png)

<HTML xmlns="http://www.w3.org/TR/REC-html40" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"><HEAD><META charset="utf-8" content="text/html" http-equiv="Content-Type"/><!--[if !mso]>
<style>
v\:* {behavior:url(#default#VML);}
o\:* {behavior:url(#default#VML);}
w\:* {behavior:url(#default#VML);}
.shape {behavior:url(#default#VML);}
</style>
<![endif]
--><STYLE><!--p.0
{mso-style-name:"Normal";line-height:570%;margin-left:0.0pt;margin-right:0.0pt;text-indent:0.0pt;margin-top:0.0pt;margin-bottom:10.0pt;text-align:justify;word-break:break-hangul;layout-grid-mode:both;vertical-align:baseline;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:10.0pt;color:#000000;mso-font-kerning:1.0pt;}
--></STYLE></HEAD><BODY><!--StartFragment--><P class="0" style="line-height:160%;margin-bottom:0.0pt;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><TABLE style="border-collapse:collapse;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;margin-left:121.95ptmso-table-overlap:never;"><TR><TD style="width:31.65pt;height:12.25pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">X</SPAN><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;vertical-align:sub;">1</SPAN></P></TD><TD style="width:29.90pt;height:12.25pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">X</SPAN><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;vertical-align:sub;">2</SPAN></P></TD><TD style="width:29.90pt;height:12.25pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">Y</SPAN></P></TD></TR><TR><TD style="width:31.65pt;height:12.25pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD><TD style="width:29.90pt;height:12.25pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD><TD style="width:29.90pt;height:12.25pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD></TR><TR><TD style="width:31.65pt;height:12.25pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD><TD style="width:29.90pt;height:12.25pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD><TD style="width:29.90pt;height:12.25pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD></TR><TR><TD style="width:31.65pt;height:4.65pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;font-size:8.0pt;"> </SPAN><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD><TD style="width:29.90pt;height:4.65pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD><TD style="width:29.90pt;height:4.65pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD></TR><TR><TD style="width:31.65pt;height:4.65pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD><TD style="width:29.90pt;height:4.65pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD><TD style="width:29.90pt;height:4.65pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD></TR></TABLE></P><!--EndFragment--></BODY></HTML>

<HTML xmlns="http://www.w3.org/TR/REC-html40" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"><HEAD><META charset="utf-8" content="text/html" http-equiv="Content-Type"/><!--[if !mso]>
<style>
v\:* {behavior:url(#default#VML);}
o\:* {behavior:url(#default#VML);}
w\:* {behavior:url(#default#VML);}
.shape {behavior:url(#default#VML);}
</style>
<![endif]
--><STYLE><!--p.0
{mso-style-name:"Normal";line-height:570%;margin-left:0.0pt;margin-right:0.0pt;text-indent:0.0pt;margin-top:0.0pt;margin-bottom:10.0pt;text-align:justify;word-break:break-hangul;layout-grid-mode:both;vertical-align:baseline;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:10.0pt;color:#000000;mso-font-kerning:1.0pt;}
--></STYLE></HEAD><BODY><!--StartFragment--><P class="0" style="line-height:160%;margin-bottom:0.0pt;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><TABLE style="border-collapse:collapse;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;mso-table-anchor-vertical:paragraph;mso-table-top:17.90pt;mso-table-anchor-horizontal:page;mso-table-left:337.40pt;"><TR><TD style="width:28.20pt;height:2.82pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">X</SPAN><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;vertical-align:sub;">1</SPAN></P></TD><TD style="width:28.35pt;height:2.82pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">X</SPAN><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;vertical-align:sub;">2</SPAN></P></TD><TD style="width:28.35pt;height:2.82pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">Y</SPAN></P></TD></TR><TR><TD style="width:28.20pt;height:2.82pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD><TD style="width:28.35pt;height:2.82pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD><TD style="width:28.35pt;height:2.82pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD></TR><TR><TD style="width:28.20pt;height:2.82pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD><TD style="width:28.35pt;height:2.82pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD><TD style="width:28.35pt;height:2.82pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD></TR><TR><TD style="width:28.20pt;height:5.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD><TD style="width:28.35pt;height:5.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD><TD style="width:28.35pt;height:5.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD></TR><TR><TD style="width:28.20pt;height:5.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD><TD style="width:28.35pt;height:5.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD><TD style="width:28.35pt;height:5.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD></TR></TABLE></P><!--EndFragment--></BODY></HTML>

<HTML xmlns="http://www.w3.org/TR/REC-html40" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"><HEAD><META charset="utf-8" content="text/html" http-equiv="Content-Type"/><!--[if !mso]>
<style>
v\:* {behavior:url(#default#VML);}
o\:* {behavior:url(#default#VML);}
w\:* {behavior:url(#default#VML);}
.shape {behavior:url(#default#VML);}
</style>
<![endif]
--><STYLE><!--p.0
{mso-style-name:"Normal";line-height:570%;margin-left:0.0pt;margin-right:0.0pt;text-indent:0.0pt;margin-top:0.0pt;margin-bottom:10.0pt;text-align:justify;word-break:break-hangul;layout-grid-mode:both;vertical-align:baseline;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:10.0pt;color:#000000;mso-font-kerning:1.0pt;}
--></STYLE></HEAD><BODY><!--StartFragment--><P class="0" style="line-height:160%;margin-bottom:0.0pt;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><TABLE style="border-collapse:collapse;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;margin-left:153.10ptmso-table-overlap:never;"><TR><TD style="width:37.85pt;height:12.45pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">X</SPAN><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;vertical-align:sub;">2</SPAN></P></TD><TD style="width:37.85pt;height:12.45pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">Y</SPAN></P></TD></TR><TR><TD style="width:37.85pt;height:12.45pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD><TD style="width:37.85pt;height:12.45pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD></TR><TR><TD style="width:37.85pt;height:12.45pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD><TD style="width:37.85pt;height:12.45pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD></TR></TABLE></P><!--EndFragment--></BODY></HTML>

<HTML xmlns="http://www.w3.org/TR/REC-html40" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"><HEAD><META charset="utf-8" content="text/html" http-equiv="Content-Type"/><!--[if !mso]>
<style>
v\:* {behavior:url(#default#VML);}
o\:* {behavior:url(#default#VML);}
w\:* {behavior:url(#default#VML);}
.shape {behavior:url(#default#VML);}
</style>
<![endif]
--><STYLE><!--p.0
{mso-style-name:"Normal";line-height:570%;margin-left:0.0pt;margin-right:0.0pt;text-indent:0.0pt;margin-top:0.0pt;margin-bottom:10.0pt;text-align:justify;word-break:break-hangul;layout-grid-mode:both;vertical-align:baseline;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:10.0pt;color:#000000;mso-font-kerning:1.0pt;}
--></STYLE></HEAD><BODY><!--StartFragment--><P class="0" style="line-height:160%;margin-bottom:0.0pt;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><TABLE style="border-collapse:collapse;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;mso-table-anchor-vertical:paragraph;mso-table-top:-42.65pt;mso-table-anchor-horizontal:page;mso-table-left:327.80pt;"><TR><TD style="width:37.30pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">X</SPAN><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;vertical-align:sub;">2</SPAN></P></TD><TD style="width:37.30pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">Y</SPAN></P></TD></TR><TR><TD style="width:37.30pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD><TD style="width:37.30pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD></TR><TR><TD style="width:37.30pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD><TD style="width:37.30pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD></TR></TABLE></P><!--EndFragment--></BODY></HTML>

<HTML xmlns="http://www.w3.org/TR/REC-html40" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"><HEAD><META charset="utf-8" content="text/html" http-equiv="Content-Type"/><!--[if !mso]>
<style>
v\:* {behavior:url(#default#VML);}
o\:* {behavior:url(#default#VML);}
w\:* {behavior:url(#default#VML);}
.shape {behavior:url(#default#VML);}
</style>
<![endif]
--><STYLE><!--p.0
{mso-style-name:"Normal";line-height:570%;margin-left:0.0pt;margin-right:0.0pt;text-indent:0.0pt;margin-top:0.0pt;margin-bottom:10.0pt;text-align:justify;word-break:break-hangul;layout-grid-mode:both;vertical-align:baseline;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:10.0pt;color:#000000;mso-font-kerning:1.0pt;}
--></STYLE></HEAD><BODY><!--StartFragment--><P class="0" style="line-height:160%;margin-bottom:0.0pt;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><TABLE style="border-collapse:collapse;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;margin-left:153.10ptmso-table-overlap:never;"><TR><TD style="width:37.05pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">X</SPAN><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;vertical-align:sub;">2</SPAN></P></TD><TD style="width:37.05pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">Y</SPAN></P></TD></TR><TR><TD style="width:37.05pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD><TD style="width:37.05pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD></TR><TR><TD style="width:37.05pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD><TD style="width:37.05pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD></TR></TABLE></P><!--EndFragment--></BODY></HTML>

<HTML xmlns="http://www.w3.org/TR/REC-html40" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word"><HEAD><META charset="utf-8" content="text/html" http-equiv="Content-Type"/><!--[if !mso]>
<style>
v\:* {behavior:url(#default#VML);}
o\:* {behavior:url(#default#VML);}
w\:* {behavior:url(#default#VML);}
.shape {behavior:url(#default#VML);}
</style>
<![endif]
--><STYLE><!--p.0
{mso-style-name:"Normal";line-height:570%;margin-left:0.0pt;margin-right:0.0pt;text-indent:0.0pt;margin-top:0.0pt;margin-bottom:10.0pt;text-align:justify;word-break:break-hangul;layout-grid-mode:both;vertical-align:baseline;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:10.0pt;color:#000000;mso-font-kerning:1.0pt;}
--></STYLE></HEAD><BODY><!--StartFragment--><P class="0" style="line-height:160%;margin-bottom:0.0pt;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><TABLE style="border-collapse:collapse;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;mso-table-anchor-vertical:paragraph;mso-table-top:24.56pt;mso-table-anchor-horizontal:page;mso-table-left:328.30pt;"><TR><TD style="width:37.30pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">X</SPAN><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;vertical-align:sub;">2</SPAN></P></TD><TD style="width:37.30pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">Y</SPAN></P></TD></TR><TR><TD style="width:37.30pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD><TD style="width:37.30pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">T</SPAN></P></TD></TR><TR><TD style="width:37.30pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD><TD style="width:37.30pt;height:11.30pt;padding:1.41pt 5.10pt 1.41pt 5.10pt;border-top:solid #0a0000 0.56pt;border-left:solid #0a0000 0.56pt;border-bottom:solid #0a0000 0.56pt;border-right:solid #0a0000 0.56pt;background:#ffffff;" valign="top"><P class="0" style="line-height:100%;margin-bottom:0.0pt;text-align:center;mso-pagination:none;text-autospace:none;mso-padding-alt:0.0pt 0.0pt 0.0pt 0.0pt;"><SPAN lang="EN-US" style="font-family:맑은 고딕;mso-font-width:100%;letter-spacing:0.0pt;mso-text-raise:0.0pt;font-size:8.0pt;">F</SPAN></P></TD></TR></TABLE></P><!--EndFragment--></BODY></HTML>

![image](https://user-images.githubusercontent.com/26988563/162415733-3d9bd246-d3d9-44f8-a7cd-6aaa8bee8553.png)
![image](https://user-images.githubusercontent.com/26988563/162415798-fee77031-eba6-4cea-b3f8-e3fc6ef70220.png)
![image](https://user-images.githubusercontent.com/26988563/162415814-eadbdc7d-f07e-49cf-9208-3bea684f1c19.png)




