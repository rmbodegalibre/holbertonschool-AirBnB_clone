<h1>AirBnB clone - The console</h1>
<p>First step: Write a command interpreter to manage your AirBnB objects.</p>
<p>This is the first step towards building your first full web application: the&nbsp;<strong>AirBnB clone</strong>. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration&hellip;</p>
<p>Each task is linked and will help you to:</p>
<ul>
<li>put in place a parent class (called&nbsp;<code>BaseModel</code>) to take care of the initialization, serialization and deserialization of your future instances</li>
<li>create a simple flow of serialization/deserialization: Instance &lt;-&gt; Dictionary &lt;-&gt; JSON string &lt;-&gt; file</li>
<li>create all classes used for AirBnB (<code>User</code>,&nbsp;<code>State</code>,&nbsp;<code>City</code>,&nbsp;<code>Place</code>&hellip;) that inherit from&nbsp;<code>BaseModel</code></li>
<li>create the first abstracted storage engine of the project: File storage.</li>
<li>create all unittests to validate all our classes and storage engine</li>
</ul>
<h3>What&rsquo;s a command interpreter?</h3>
<p>Do you remember the Shell? It&rsquo;s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:</p>
<ul>
<li>Create a new object (ex: a new User or a new Place)</li>
<li>Retrieve an object from a file, a database etc&hellip;</li>
<li>Do operations on objects (count, compute stats, etc&hellip;)</li>
<li>Update attributes of an object</li>
<li>Destroy an object</li>
</ul>
<h2 dir="auto">Installation</h2>
<p dir="auto">Clone the repository and run the console.py</p>
<div class="snippet-clipboard-content notranslate position-relative overflow-auto">
<pre class="notranslate"><code>$ git clone <br /></code></pre>
</div>
<h4 dir="auto">How to Use Command Interpreter</h4>
<hr />
<table>
<thead>
<tr>
<th>Commands</th>
<th>Sample Usage</th>
<th>Functionality</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>help</code></td>
<td><code>help</code></td>
<td>displays all commands available</td>
</tr>
<tr>
<td><code>create</code></td>
<td><code>create &lt;class&gt;</code></td>
<td>creates new object (ex. a new User, Place)</td>
</tr>
<tr>
<td><code>update</code></td>
<td><code>User.update('123', {'name' : 'Greg_n_Mel'})</code></td>
<td>updates attribute of an object</td>
</tr>
<tr>
<td><code>destroy</code></td>
<td><code>User.destroy('123')</code></td>
<td>destroys specified object</td>
</tr>
<tr>
<td><code>show</code></td>
<td><code>User.show('123')</code></td>
<td>retrieve an object from a file, a database</td>
</tr>
<tr>
<td><code>all</code></td>
<td><code>User.all()</code></td>
<td>display all objects in class</td>
</tr>
<tr>
<td><code>count</code></td>
<td><code>User.count()</code></td>
<td>returns count of objects in specified class</td>
</tr>
<tr>
<td><code>quit</code></td>
<td><code>quit</code></td>
<td>exits</td>
</tr>
</tbody>
</table>
<h2>More Info</h2>
<h3>Execution</h3>
<p>Your shell should work like this in interactive mode:</p>
<pre><code>$ ./console.py
(hbnb) help

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
</code></pre>
<p>But also in non-interactive mode: (like the Shell project in C)</p>
<pre><code>$ echo "help" | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help &lt;topic&gt;):
========================================
EOF  help  quit
(hbnb) 
$
</code></pre>
<p>All tests should also pass in non-interactive mode:&nbsp;<code>$ echo "python3 -m unittest discover tests" | bash</code></p>
<p>&nbsp;</p>
<h2 dir="auto">Examples</h2>
<p dir="auto">To run... In command line of terminal, in path (holbertonschool-AirBnB_clone/) write: ./console.py</p>
<p dir="auto">then... The prompt of the console appears:</p>
<p dir="auto"><code>(hbnb)</code></p>
<p dir="auto">... in this prompt you can write any available command. Ex:</p>
<p dir="auto"><code>(hbnb) help</code></p>
<p dir="auto">... After pressing the Enter key, you will see the result:</p>
<code>
<p>(hbnb) help</p>
<p>Documented commands (type help &lt;topic&gt;):<br />
  ========================================<br />
  EOF  all  count  create  destroy  help  quit  show  update</p>
<p>(hbnb) </p></code>
<p dir="auto">You can use help with another command to find its info.</p>
<p dir="auto"><code>(hbnb) help</code> quit</p>
<p dir="auto">... After pressing the Enter key, you will see the result:</p>
<p dir="auto"><code>(hbnb) help quit<br />
Quit command to exit the program</code></p>
<p dir="auto">&nbsp;</p>
<h2 dir="auto">Serialization</h2>
<p dir="auto">Serialization is the process of converting an object into a sequence of bytes for storage or transmission to memory, a database, or a file. Its main purpose is to save the state of an object so that it can be recreated when needed. The reverse process is called deserialization.</p>
<h2>Serializing JSON</h2>
<p>  What happens after a computer processes a lot of information? You need to take a data dump. Consequently, the json library exposes the dump() method to write data to files. There is also a dumps() method (pronounced like “dump-s”) for writing to a Python string.</p>
<p>Simple Python objects are translated to JSON according to a fairly intuitive conversion.</p>
<table>
  <thead>
    <tr>
      <th width="133">Python</th>
      <th width="121">JSON</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>dict</td>
      <td>object</td>
    </tr>
    <tr>
      <td>list, tuple</td>
      <td>array</td>
    </tr>
    <tr>
      <td>str</td>
      <td>string</td>
    </tr>
    <tr>
      <td>int, long, float</td>
      <td>number</td>
    </tr>
    <tr>
      <td>True</td>
      <td>true</td>
    </tr>
    <tr>
      <td>False</td>
      <td>false</td>
    </tr>
    <tr>
      <td>None</td>
      <td>null</td>
    </tr>
  </tbody>
</table>
<h2>A simple serialization example</h2>
<p>Imagine that you are working with a Python object in memory that looks like this:</p>
<pre title="" tabindex="0">data = {
    &quot;president&quot;: {
        &quot;name&quot;: &quot;Zaphod Beeblebrox&quot;,
        &quot;spice&quot;: &quot;Betelgeusian&quot;
    }
}<span aria-hidden="true">      </span></pre>
<p>Es fundamental que guarde esta información en el disco, por lo que su misión es escribirla en un archivo.</p>
<p>It is critical that you save this information to disk, so your mission is to write it to a file.</p>
<p>Using Python's context manager, you can create a file called file_data.json and open it in write mode. (JSON files conveniently end in a .json extension.)</p>
<pre tabindex="0">with open(&quot;file_data.json&quot;, &quot;w&quot;) as write_file:
    json.dump(data, write_file)<span aria-hidden="true">  </span></pre>
<p>Note that dump() takes two positional arguments:  the data object to be serialized, and (2) the file-like object to which the bytes will be written.</p>
<p>Or, if you were so inclined to continue using this serialized JSON data in your program, you could write it to a native Python str object.</p>
<pre tabindex="0">json_string = json.dumps(data)<span aria-hidden="true"> </span></pre>
<p>Note that the file-like object is missing since it's not actually writing to disk. Other than that, dumps() is just like dump().</p>
<p dir="auto">&nbsp;</p>
<h2 dir="auto">Deserialization</h2>
<p dir="auto">Deserialization consists of converting a string into a Python object (usually a list or dictionary).</p>
<h2>Deserializando JSON</h2>
<p>In the json library, you'll find load() and loads() to convert JSON-encoded data into Python objects.</p>
<p>Like serialization, there is a simple conversion table for deserialization, although you can probably already guess what it looks like.</p>
<table>
  <thead>
    <tr>
      <th width="138">JSON</th>
      <th width="130">Python</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>object</td>
      <td>dict</td>
    </tr>
    <tr>
      <td>array</td>
      <td>list</td>
    </tr>
    <tr>
      <td>string</td>
      <td>str</td>
    </tr>
    <tr>
      <td>number (int)</td>
      <td>int</td>
    </tr>
    <tr>
      <td>number (real)</td>
      <td>float</td>
    </tr>
    <tr>
      <td>true</td>
      <td>True</td>
    </tr>
    <tr>
      <td>false</td>
      <td>False</td>
    </tr>
    <tr>
      <td>null</td>
      <td>None</td>
    </tr>
  </tbody>
</table>
<p>Technically, this conversion is not the perfect inverse of the serialization table. Basically that means that if you encode an object now and then decode it again, you may not get exactly the same object.</p>
<h2>A simple deserialization example</h2>
<p>This time, imagine that you have some data stored on disk that you would like to manipulate in memory. It will still use the context manager, but this time it will open the existing data.json_file in read mode.</p>
<pre tabindex="0">with open(&quot;archivo_data.json&quot;, &quot;r&quot;) as read_file:
    data = json.load(read_file)<span aria-hidden="true">  </span></pre>
<p>Things are pretty straightforward here, but be aware that the result of this method could return any of the lookup table's allowed data types. This is only important if you're loading data that you haven't seen before. In most cases, the root object will be a dict or a list.</p>
<p>If you've pulled JSON data from another program or gotten a JSON-formatted string from Python, you can easily deserialize it with loads(), which naturally loads from a string:</p>
<pre tabindex="0">json_string = &quot;&quot;&quot;
{
    &quot;researcher&quot;: {
        &quot;name&quot;: &quot;Ford Prefect&quot;,
        &quot;species&quot;: &quot;Betelgeusian&quot;,
        &quot;relatives&quot;: [
            {
                &quot;name&quot;: &quot;Zaphod Beeblebrox&quot;,
                &quot;species&quot;: &quot;Betelgeusian&quot;
            }
        ]
    }
}  &quot;&quot;&quot;  data = json.loads(json_string)</pre>
<h1 id="modulos-y-paquetes">Modules and packages</h1>
<h2 id="modulos">modules</h2>
<p>A <em>module</em> is a Python file whose objects (functions, classes, exceptions, etc.) can be accessed from another file. It is simply a way of organizing large codes.</p>
<p>Consider, for example, a file aritmetica.pycontaining the following definitions.</p>
<p><code>def sum(a, b):</code></p>
<p>  <code> return a + b    </code></p>
<p><code>def subs(a, b):</code></p>
<p><code> return a - b    </code></p>
<p><code>def mult(a, b):</code></p>
<p><code> return a * b    </code></p>
<p><code>def div(a, b):</code></p>
<p><code> return a / b</code></p>
<p>We can access them from another Python file located in the same path by <em>importing</em> the module.</p>
<pre>import aritmetica
    print(aritmetica.sum(7, 5))  </pre>
<p>An alternative syntax for importing objects from a module is as follows.</p>
<pre>from aritmetica import sum
    print(sum(7, 5))  </pre>
<p>Note that, in this second case, the module name is not prefixed when invoking the imported object. We can import multiple objects by separating them by commas.</p>
<pre>from aritmetica import sum, subs, mult, div

    print(sum(7, 5))
    print(subs(7, 5))
    print(mult(7, 5))
    print(div(7, 5))  </pre>
<p>Or, to import all objects within a module:</p>
<pre>from aritmetica import *  </pre>
<p>We can make a module visible to <em>any</em> file by placing it in the folder Libinside the Python installation directory (eg C:\Python310\Lib).</p>
<h2 id="paquetes">packages</h2>
<p>A <em>package</em> is a folder that contains multiple modules. Following the example above, we can design a package matematicaby creating a folder with the following structure.</p>
<pre>matematica/
      |-- __init__.py
      |-- aritmetica.py
      |-- geometria.py  </pre>
<p>It must always contain a file __init__.py(empty at the moment) so that Python understands that it is a package and not just a folder. Thus, we can access some of the package modules as follows.</p>
<pre>import matematica.aritmetica

    print(matematica.aritmetica.sum(7, 5))  </pre>
<p>Or the next.</p>
<pre>from matematica import aritmetica

    print(aritmetica.sum(7, 5))  </pre>
<p>Also, this other one:</p>
<pre>from matematica.aritmetica import sum

    print(sum(7, 5))</pre>
<p dir="auto">&nbsp;</p>
<h2 dir="auto">Cyclical imports</h2>
<p dir="auto">A circular import occurs when from one module A you import another module B (because it needs a function or variable that is in B, but module B in turn needs to use a function or variable that is in module A, so it also tries to import it .</p>
<pre># Module A
import B

def function_in_A():
    result = B.function_in_B()
    print(result)
A_CONFIG = &quot;Hello&quot;  </pre>
<pre># Module B
import A
    def function_in_B():
    return A.A_CONFIG +  &quot; world&quot;</pre>
<h2>How to Use the Python import Statement</h2>
<p>The Python import statement imports code from one module into another program. You can import all the code from a module by specifying the import keyword followed by the module you want to import.</p>
<p>import statements appear at the top of a Python file, beneath any comments that may exist. This is because importing modules or packages at the top of a file makes the structure of your code clearer.</p>
<p>The syntax for the import statement is:</p>
<div>
  <pre>import [module]</pre>
</div>
<p>Let&rsquo;s look at an example of the Python import statement.</p>
<p>If we wanted to import the sys library, we could use:</p>
<div>
  <pre>import sys</pre>
</div>
<h2>import Python: Using the from Statement</h2>
<p>The import statement allows you to import all the functions from a module into your code.</p>
<p>Often, though, you&rsquo;ll only want to import a few functions, or just one. If this is the case, you can use the from statement. This lets you import only the exact functions you are going to be using in your code.</p>
<p>The syntax for using the from statement is:</p>
<div>
  <pre>from [module] import [function or value]</pre>
</div>
<p>Suppose we only want to import the choice() function from the &ldquo;random&rdquo; library into our code. We could do so like this:</p>
<div>
  <pre>from random import choice    fruits = [&quot;Apple&quot;, &quot;Pear&quot;, &quot;Banana&quot;]    print(choice(fruits))  </pre>
</div>
<p>Our code returns:</p>
<div>
  <pre>Pear</pre>
</div>
<p>We use the <em>from</em> keyword, followed by <em>random</em>, to tell our program that we want to import a specific function from the &ldquo;random&rdquo; module. Then, we use the <em>import</em> keyword to tell our code what function we want to import.</p>
<p>When using the <em>from</em> keyword to import a function, you do not need to write the function using dot notation. As you can see above, instead of using <em>random.choice()</em> to access the <em>random.choice()</em> function from the random module, we just use <em>choice()</em>.</p>
<h2 dir="auto">Clean Code &iquest;what is it?</h2>
<div id="c267249">
  <div class="text-row ce-textpic ce-center ce-above">
<div class="ce-bodytext">
<p><span>Clean&nbsp;</span><em><span>code</span></em><span>&nbsp;is not a set of strict rules, but rather a set of principles that help produce code that is intuitive and easy to modify.&nbsp;In this context, intuitive means that any professional developer can immediately understand it.&nbsp;An easily adaptable code has the following characteristics:</span></p>
<ul>
<li><span>The&nbsp;</span><strong><span>execution sequence of</span></strong><span>&nbsp;the entire program follows a&nbsp;</span><strong><span>logical</span></strong><span>&nbsp;and</span><span>it has a&nbsp;</span><strong><span>simple structure</span></strong><span>&nbsp;.</span></li>
<li><span>The&nbsp;</span><strong><span>relationship</span></strong><span>&nbsp;between the different parts of the code is&nbsp;</span><strong><span>clearly visible</span></strong><span>&nbsp;.</span></li>
<li><span>The&nbsp;</span><strong><span>task or function</span></strong><span>&nbsp;of each class, function, method and variable is&nbsp;</span><strong><span>understandable at first glance</span></strong><span>&nbsp;.</span></li>
</ul>
<p><span>A code is considered easy to modify when it is flexible and extensible, which also helps to correct possible errors that it may have.&nbsp;For all these reasons, clean code is very easy to maintain and has the following properties:</span></p>
<ul>
<li><span>Classes and methods are&nbsp;</span><strong><span>reduced</span></strong><span>&nbsp;and, if possible, have a single clear task.</span></li>
<li><span>Classes and methods are&nbsp;</span><strong><span>predictable</span></strong><span>&nbsp;, work as expected, and are publicly accessible through well-documented APIs (interfaces).</span></li>
<li><span>The code has been subjected to&nbsp;&nbsp;</span><strong><a href="https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/el-papel-del-unit-test-en-el-desarrollo-de-software/"><span>unit tests</span></a></strong><span>&nbsp;.</span></li>
</ul>
</div>
</div>
</div>
<div id="c267250">
<div class="text-row ce-textpic ce-center ce-above">
<div class="ce-bodytext">
<p>The advantages of this type of programming are obvious: the&nbsp;<em>clean code</em>&nbsp;becomes&nbsp;<strong>independent of the developer who created it</strong>&nbsp;.&nbsp;In principle, any programmer can work with it, which avoids problems such as those associated with&nbsp;&nbsp;<a title="What is the legacy code?" href="https://www.ionos.es/digitalguide/paginas-web/desarrollo-web/que-es-el-legacy-code/">legacy code</a>&nbsp;.&nbsp;Software&nbsp;<strong>maintenance is also simplified</strong>&nbsp;, because&nbsp;<em>bugs</em>&nbsp;are easier to find and fix.</p>
<h2 dir="auto">Comments</h2>
<p><span>Comments are always helpful when writing code.&nbsp;</span><span>We use them for various purposes: from commenting on a line or block of code that doesn't work, to leaving small reminders such as tasks to do or explanations for our future selves.&nbsp;</span><span>All programming languages ​​allow you to add comments, and of course Python is no exception.</span></p>
</div>
</div>
</div>
<h2 dir="auto"><a id="user-content-bugs" class="anchor" aria-hidden="true"></a>Bugs</h2>
<p style="color: #5e9ca0;"><span style="color: #000000;">Here is a small list of bugs that were fixed. This program is still under review.</span></p>
<h2 dir="auto"><a id="user-content-files" class="anchor" aria-hidden="true"></a>Files</h2>
<p style="color: #5e9ca0;"><span style="color: #000000;">Files include are:</span><br /><span style="color: #000000;">README.md<br />AUTHORS<br />console.py<br />tests/<br />models/__init__.py<br />models/base_model.py<br />models/user.py<br />models/state.py<br />models/city.py<br />models/amenity.py<br />models/place.py<br /></span><span style="color: #000000;">models/review.py<br />models/engine/__init__.py<br />models/engine/file_storage.py<br /></span></p>
<h2 dir="auto"><a id="user-content-history" class="anchor" aria-hidden="true"></a>History</h2>
<p style="color: #5e9ca0;"><span style="color: #000000;">This is the first version</span></p>
<h2 dir="auto"><a id="user-content-authors" class="anchor" aria-hidden="true"></a>Authors</h2>
<p style="color: #5e9ca0;"><span style="color: #000000;">Written by David Stiven Perlaza &amp; Ricardo Monta&ntilde;a.</span><br /><span style="color: #000000;">October 28th, 2022</span></p>
<h2 dir="auto"><a id="user-content-copyright" class="anchor" aria-hidden="true"></a>Copyright</h2>
<p style="color: #5e9ca0;"><span style="color: #000000;">&copy; All rights reserved</span></p>
<p>&nbsp;</p>