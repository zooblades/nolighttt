package local.nolight.mixin;

import net.minecraft.client.multiplayer.ClientLevel;
import net.minecraft.core.Direction;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

@Mixin(ClientLevel.class)
public class NoShadeMixin {
	@Inject(method = "getShade", at = @At("HEAD"), cancellable = true)
	private void nolight$noShade(Direction direction, boolean shade, CallbackInfoReturnable<Float> cir) {
		cir.setReturnValue(1.0F);
	}
}
