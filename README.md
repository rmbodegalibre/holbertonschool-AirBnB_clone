<h1 class="gap">0x00. AirBnB clone - The console</h1>
<p>&nbsp;</p>
<h4>First step: Write a command interpreter to manage your AirBnB objects.</h4>
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
<p dir="auto">To run</p>
<h2 dir="auto">Serialization</h2>
<h2 dir="auto">&nbsp;</h2>
<h2 dir="auto">Deserialization</h2>
<p dir="auto">&nbsp;</p>
<ul>
<li>Serialization / Deserialization flow (object &lt;-&gt; Dict &lt;-&gt; Json &lt;-&gt; file)</li>
</ul>
<h2 dir="auto">Packages, Modules, Cyclical imports, How to Import, prevent excecution</h2>
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