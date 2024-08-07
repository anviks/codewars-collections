<p><img alt="Gameplay screencap" src="https://i.imgur.com/mYgmiOz.jpg"></p>
<p><a style="color:#9f9;text-decoration:none" href="https://en.wikipedia.org/wiki/Papers%2C_Please" data-turbolinks="false" target="_blank"><b>Papers, Please</b></a> is an indie video game where the player takes on a the role of a border crossing immigration officer in the fictional dystopian Eastern Bloc-like country of Arstotzka in the year 1982. As the officer, the player must review each immigrant and returning citizen's passports and other supporting paperwork against a list of ever-increasing rules using a number of tools and guides, allowing in only those with the proper paperwork, rejecting those without all proper forms, and at times detaining those with falsified information.</p>

<h2 style="color:#f88">Objective</h2>
<p>Your task is to create a constructor function (or class) and a set of instance methods to perform the tasks of the border checkpoint inspection officer. The methods you will need to create are as follow:</p>

<h3>Method: <span style="color:#8df">receiveBulletin</span></h3>
<p>Each morning you are issued an official bulletin from the Ministry of Admission. This bulletin will provide updates to regulations and procedures and the name of a wanted criminal.</p>
<p>The bulletin is provided in the form of a <code>string</code>. It may include one or more of the following:</p>

<ul>
<li>Updates to the list of nations (comma-separated if more than one) whose citizens may enter (begins empty, before the first bulletin):<pre><code>example 1: Allow citizens of Obristan
example 2: Deny citizens of Kolechia, Republia
</code></pre>
</li>
<li>Updates to required documents<pre><code>example 1: Foreigners require access permit
example 2: Citizens of Arstotzka require ID card
example 3: Workers require work pass
</code></pre>
</li>
<li>Updates to required vaccinations<pre><code>example 1: Citizens of Antegria, Republia, Obristan require polio vaccination
example 2: Entrants no longer require tetanus vaccination
</code></pre>
</li>
<li>Update to a currently wanted criminal<pre><code>example 1: Wanted by the State: Hubert Popovic
</code></pre>
</li>
</ul>
<h3>Method: <span style="color:#8df">inspect</span></h3>
<p>Each day, a number of entrants line up outside the checkpoint inspection booth to gain passage into Arstotzka. The <code>inspect</code> method will receive an object representing each entrant's set of identifying documents. This object will contain zero or more properties which represent separate documents. Each property will be a <code>string</code> value. These properties may include the following:</p>
<ul>
    <li>Applies to all entrants:
        <ul>
            <li><code>passport</code></li>
            <li><code>certificate_of_vaccination</code></li>
        </ul>
    </li>
    <li>Applies only to citizens of Arstotzka
        <ul><li><code>ID_card</code></li></ul>
    </li>
    <li>Applies only to foreigners:
        <ul>
            <li><code>access_permit</code></li>
            <li><code>work_pass</code></li>
            <li><code>grant_of_asylum</code></li>
            <li><code>diplomatic_authorization</code></li>
        </ul>
    </li>
</ul>

<p>The <code>inspect</code> method will return a result based on whether the entrant passes or fails inspection:</p>
<p><b>Conditions for passing inspection</b></p>
<ul>
    <li>All required documents are present</li>
    <li>There is no conflicting information across the provided documents</li>
    <li>All documents are current (ie. none have expired) -- a document is considered expired if the expiration date is <code>November 22, 1982</code> or earlier</li>
    <li>The entrant is not a wanted criminal</li>
    <li>If a <code>certificate_of_vaccination</code> is required and provided, it must list the required vaccination</li>
    <li>A "worker" is a foreigner entrant who has <code>WORK</code> listed as their purpose on their access permit</li>
    <li>If entrant is a foreigner, a <code>grant_of_asylum</code> or <code>diplomatic_authorization</code> are acceptable in lieu of an <code>access_permit</code>. In the case where a <code>diplomatic_authorization</code> is used, it must include <code>Arstotzka</code> as one of the list of nations that can be accessed.</li>
</ul>
<p>If the entrant <span style="color:#0f0">passes</span> inspection, the method should return one of the following <code>string</code> values:</p>
<ul>
    <li>If the entrant is a citizen of Arstotzka: <code>Glory to Arstotzka.</code></li>
    <li>If the entrant is a foreigner: <code>Cause no trouble.</code></li>
</ul>

<p>If the entrant <span style="color:#f66">fails</span> the inspection due to expired or missing documents, or their <code>certificate_of_vaccination</code> does not include the necessary vaccinations, return <code>Entry denied:</code> with the reason for denial appended.</p>
<pre><code>Example 1: Entry denied: passport expired.
Example 2: Entry denied: missing required vaccination.
Example 3: Entry denied: missing required access permit.
</code></pre>
<p>If the entrant <span style="color:#f66">fails</span> the inspection due to mismatching information between documents (causing suspicion of forgery) or if they're a wanted criminal, return <code>Detainment:</code> with the reason for detainment appended.</p>
<ul>
    <li>If due to information mismatch, include the mismatched item. e.g.<code>Detainment: ID number mismatch.</code></li>
    <li>If the entrant is a wanted criminal: <code>Detainment: Entrant is a wanted criminal.</code></li>
    <li><b>NOTE:</b> One wanted criminal will be specified in each daily bulletin, and must be detained when received for that day only. For example, if an entrant on Day 20 has the same name as a criminal declared on Day 10, they are not to be detained for being a criminal.<br>Also, if any of an entrant's identifying documents include the name of that day's wanted criminal (in case of mismatched names across multiple documents), they are assumed to be the wanted criminal.</li>
</ul>

<p>In some cases, there may be multiple reasons for denying or detaining an entrant. For this exercise, you will only need to provide one reason.</p>
<ul>
    <li>If the entrant meets the criteria for both entry denial and detainment, priority goes to detaining.<br>
    For example, if they are missing a required document and are also a wanted criminal, then they should be detained instead of turned away.</li>
    <li>In the case where the entrant has mismatching information and is a wanted criminal, detain for being a wanted criminal.</li>
</ul>

<h2 style="color:#f88">Test Example</h2>

<pre style="display: none;"><code class="language-javascript"><span class="cm-keyword">const</span> <span class="cm-def">bulletin</span> <span class="cm-operator">=</span> <span class="cm-string-2">`Entrants require passport</span>
<span class="cm-string-2">Allow citizens of Arstotzka, Obristan`</span>;

<span class="cm-keyword">const</span> <span class="cm-def">inspector</span> <span class="cm-operator">=</span> <span class="cm-keyword">new</span> <span class="cm-variable">Inspector</span>();
<span class="cm-variable">inspector</span>.<span class="cm-property">receiveBulletin</span>(<span class="cm-variable">bulletin</span>);

<span class="cm-keyword">const</span> <span class="cm-def">entrant1</span> <span class="cm-operator">=</span> {
    <span class="cm-property">passport</span>:<span class="cm-string-2">`ID#: GC07D-FU8AR</span>
    <span class="cm-string-2">NATION: Arstotzka</span>
    <span class="cm-string-2">NAME: Guyovich, Russian</span>
    <span class="cm-string-2">DOB: 1933.11.28</span>
    <span class="cm-string-2">SEX: M</span>
    <span class="cm-string-2">ISS: East Grestin</span>
    <span class="cm-string-2">EXP: 1983.07.10`</span>
};

<span class="cm-variable">inspector</span>.<span class="cm-property">inspect</span>(<span class="cm-variable">entrant1</span>); <span class="cm-comment">//'Glory to Arstotzka.'</span>
</code></pre>
<pre><code class="language-python"><span class="cm-variable">bulletin</span> <span class="cm-operator">=</span> <span class="cm-string">"""Entrants require passport</span>
<span class="cm-string">Allow citizens of Arstotzka, Obristan"""</span>

<span class="cm-variable">inspector</span> <span class="cm-operator">=</span> <span class="cm-variable">Inspector</span>()
<span class="cm-variable">inspector</span>.<span class="cm-property">receive_bulletin</span>(<span class="cm-variable">bulletin</span>)

<span class="cm-variable">entrant1</span> <span class="cm-operator">=</span> {
    <span class="cm-string">"passport"</span>: <span class="cm-string">"""ID#: GC07D-FU8AR</span>
<span class="cm-string">    NATION: Arstotzka</span>
<span class="cm-string">    NAME: Guyovich, Russian</span>
<span class="cm-string">    DOB: 1933.11.28</span>
<span class="cm-string">    SEX: M</span>
<span class="cm-string">    ISS: East Grestin</span>
<span class="cm-string">    EXP: 1983.07.10"""</span>
}

<span class="cm-variable">inspector</span>.<span class="cm-property">inspect</span>(<span class="cm-variable">entrant1</span>) <span class="cm-comment">#=&gt; 'Glory to Arstotzka.'</span>
</code></pre>
<pre style="display: none;"><code class="language-java"><span class="cm-type">String</span> <span class="cm-variable">bulletin</span> <span class="cm-operator">=</span> <span class="cm-string">"Entrants require passport\n"</span> <span class="cm-operator">+</span>
    <span class="cm-string">"Allow citizens of Arstotzka, Obristan"</span>;

<span class="cm-variable">Inspector</span> <span class="cm-variable">inspector</span> <span class="cm-operator">=</span> <span class="cm-keyword">new</span> <span class="cm-variable">Inspector</span>();
<span class="cm-variable">inspector</span>.<span class="cm-variable">receiveBulletin</span>(<span class="cm-variable">bulletin</span>);

<span class="cm-variable">Map</span><span class="cm-operator">&lt;</span><span class="cm-type">String</span>, <span class="cm-type">String</span><span class="cm-operator">&gt;</span> <span class="cm-variable">entrant1</span> <span class="cm-operator">=</span> <span class="cm-keyword">new</span> <span class="cm-variable">HashMap</span><span class="cm-operator">&lt;&gt;</span>();
<span class="cm-variable">entrant1</span>.<span class="cm-variable">put</span>(<span class="cm-string">"passport"</span>, <span class="cm-string">"ID#: GC07D-FU8AR\n"</span> <span class="cm-operator">+</span>
    <span class="cm-string">"NATION: Arstotzka\n"</span> <span class="cm-operator">+</span>
    <span class="cm-string">"NAME: Guyovich, Russian\n"</span> <span class="cm-operator">+</span>
    <span class="cm-string">"DOB: 1933.11.28\n"</span> <span class="cm-operator">+</span>
    <span class="cm-string">"SEX: M\n"</span> <span class="cm-operator">+</span>
    <span class="cm-string">"ISS: East Grestin\n"</span> <span class="cm-operator">+</span>
    <span class="cm-string">"EXP: 1983.07.10\n"</span>
);

<span class="cm-variable">inspector</span>.<span class="cm-variable">inspect</span>(<span class="cm-variable">entrant1</span>); <span class="cm-comment">// "Glory to Arstotzka."</span>
</code></pre>
<h2 style="color:#f88">Additional Notes</h2>

<ul>
<li>Inputs will always be valid.</li>
<li>There are a total of 7 countries: <code>Arstotzka</code>, <code>Antegria</code>, <code>Impor</code>, <code>Kolechia</code>, <code>Obristan</code>, <code>Republia</code>, and <code>United Federation</code>.</li>
<li>Not every single possible case has been listed in this Description; use the test feedback to help you handle all cases.</li>
<li>The concept of this kata is derived from the video game of the same name, but it is not meant to be a direct representation of the game.</li>
</ul>
<p>If you enjoyed this kata, be sure to check out <a href="https://www.codewars.com/users/docgunthrop/authored" data-turbolinks="false" target="_blank">my other katas</a>.</p>
