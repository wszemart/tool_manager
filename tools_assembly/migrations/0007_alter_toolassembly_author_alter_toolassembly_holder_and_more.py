# Generated by Django 4.2.3 on 2024-03-14 17:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("tools", "0002_alter_tool_d1_alter_tool_d2_alter_tool_d3_and_more"),
        ("holders", "0002_alter_holder_dh1_a_alter_holder_dh1_b_and_more"),
        ("machines", "0002_alter_machine_author_alter_machine_description_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tools_assembly", "0006_rename_toolassembly_usercomment_tool_assembly"),
    ]

    operations = [
        migrations.AlterField(
            model_name="toolassembly",
            name="author",
            field=models.ForeignKey(
                default=None,
                help_text="Author of the tool assembly.",
                on_delete=django.db.models.deletion.SET_DEFAULT,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="toolassembly",
            name="holder",
            field=models.ForeignKey(
                help_text="A holder component used in a tool assembly.",
                on_delete=django.db.models.deletion.CASCADE,
                to="holders.holder",
            ),
        ),
        migrations.AlterField(
            model_name="toolassembly",
            name="machine",
            field=models.ForeignKey(
                default=None,
                help_text="The machine to which the tool is assigned.",
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="tools",
                to="machines.machine",
            ),
        ),
        migrations.AlterField(
            model_name="toolassembly",
            name="outside_holder",
            field=models.DecimalField(
                blank=True, decimal_places=2, help_text="Length outside the holder.", max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="toolassembly",
            name="radius",
            field=models.DecimalField(
                blank=True, decimal_places=3, help_text="Radius of the tool assembly.", max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="toolassembly",
            name="tool",
            field=models.ForeignKey(
                help_text="A tool component used in a tool assembly.",
                on_delete=django.db.models.deletion.CASCADE,
                to="tools.tool",
            ),
        ),
        migrations.AlterField(
            model_name="toolassembly",
            name="tool_nr",
            field=models.PositiveIntegerField(help_text="Number of the tool assembly in machine table."),
        ),
        migrations.AlterField(
            model_name="toolassembly",
            name="total_length",
            field=models.DecimalField(
                blank=True, decimal_places=2, help_text="Total tool length.", max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="usercomment",
            name="author",
            field=models.ForeignKey(
                help_text="Author of the user comment.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="usercomment",
            name="content",
            field=models.TextField(help_text="User comment."),
        ),
        migrations.AlterField(
            model_name="usercomment",
            name="date_posted",
            field=models.DateTimeField(
                default=django.utils.timezone.now, help_text="Date the comment was published <em>YYYY-MM-DD</em>."
            ),
        ),
        migrations.AlterField(
            model_name="usercomment",
            name="tool_assembly",
            field=models.ForeignKey(
                help_text="The tool assembly to which the comment is assigned.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="tools_assembly.toolassembly",
            ),
        ),
    ]
