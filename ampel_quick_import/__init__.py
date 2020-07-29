import importlib, glob, os, re, pkg_resources
from IPython.core.magic import needs_local_scope, register_line_magic # type: ignore

ampel_folders = {
	os.path.dirname(pkg_resources.get_distribution(dist_name).module_path) # type: ignore
	for dist_name in pkg_resources.AvailableDistributions() # type: ignore
	if dist_name.startswith("pyampel") or dist_name.startswith("ampel-")
}


def load_ipython_extension(ipython):
	pass


def clsimport(modname, local_ns=None):

	clsname = modname.split(".")[-1]

	if clsname in globals():
		return

	mod = importlib.import_module(modname)
	cls = getattr(mod, clsname, None)
	if cls:
		local_ns[clsname] = cls
	else:
		print("Module %s does not define class %s" % (modname, clsname))


@register_line_magic
@needs_local_scope
def qi(line, local_ns):
	for el in line.split(" "):
		quickimport(el, local_ns)


def quickimport(clsname, local_ns=None):


	for d in ampel_folders:
		os.chdir(d)
		a = glob.glob("**/" + clsname + ".py", recursive=True)
		if len(a) != 0:
			clsimport(
				re.sub(
					".*\.ampel\.", # noqa
					"ampel.",
					a[0] \
						.replace("/", ".") \
						.replace(".py", "")
				),
				local_ns
			)
			return
	print(f"Class {clsname} not found")
