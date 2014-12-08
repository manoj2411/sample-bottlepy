<h1>Tasks list</h1>
<table>
<tr><th>Name</th> <th>Row</th></tr>
%for row in rows:
    <tr>
    %for col in row:
        <td>{{col}}</td>
    %end
    <td>{{row}}</td>
    </tr>
%end
</table>
